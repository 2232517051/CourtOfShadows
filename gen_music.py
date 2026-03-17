import struct, math, random, os

RATE = 44100

def write_wav(filename, samples, rate=RATE):
    n = len(samples)
    with open(filename, 'wb') as f:
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + n * 2))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(struct.pack('<IHHIIHH', 16, 1, 1, rate, rate * 2, 2, 16))
        f.write(b'data')
        f.write(struct.pack('<I', n * 2))
        for s in samples:
            v = max(-32768, min(32767, int(s * 32767)))
            f.write(struct.pack('<h', v))

def note_freq(semitones_from_a4):
    return 440.0 * (2 ** (semitones_from_a4 / 12.0))

notes = {
    'C3': note_freq(-21), 'D3': note_freq(-19), 'E3': note_freq(-17), 'F3': note_freq(-16),
    'G3': note_freq(-14), 'A3': note_freq(-12), 'B3': note_freq(-10),
    'C4': note_freq(-9), 'D4': note_freq(-7), 'E4': note_freq(-5), 'F4': note_freq(-4),
    'G4': note_freq(-2), 'A4': 440.0, 'B4': note_freq(2),
    'C5': note_freq(3), 'D5': note_freq(5), 'E5': note_freq(7),
    'Bb3': note_freq(-11), 'Eb4': note_freq(-6), 'Ab3': note_freq(-13),
    'Bb4': note_freq(1), 'Eb3': note_freq(-18), 'Ab4': note_freq(-1),
    'F#3': note_freq(-15), 'C#4': note_freq(-8),
}

def organ_tone(freq, t, vol=0.15):
    s = math.sin(2*math.pi*freq*t) * 0.4
    s += math.sin(2*math.pi*freq*2*t) * 0.2
    s += math.sin(2*math.pi*freq*3*t) * 0.1
    s += math.sin(2*math.pi*freq*4*t) * 0.05
    return s * vol

def string_tone(freq, t, vol=0.12):
    s = 0
    for h in range(1, 8):
        s += math.sin(2*math.pi*freq*h*t) * ((-1)**(h+1)) / h
    return s * vol * 0.5

def pad_tone(freq, t, vol=0.1):
    s = math.sin(2*math.pi*freq*t) * 0.5
    s += math.sin(2*math.pi*freq*1.002*t) * 0.5
    return s * vol

base = os.path.join(os.path.dirname(__file__), 'game', 'audio', 'music')

# 1. main_theme.wav - Epic medieval theme (Dm)
duration = 30
samples = []
chords = [
    ('D3','F3','A3'), ('Bb3','D4','F4'), ('C4','E4','G4'), ('D3','F3','A3'),
    ('D3','F3','A3'), ('F3','A3','C4'), ('C4','E4','G4'), ('D3','F3','A3'),
]
melody_notes = ['D4','F4','E4','D4','A4','G4','F4','E4','D4','F4','A4','G4','F4','E4','D4','C4']
chord_dur = duration / len(chords)
for i in range(int(duration * RATE)):
    t = i / RATE
    ci = min(int(t / chord_dur), len(chords)-1)
    chord = chords[ci]
    s = 0
    for n in chord:
        s += organ_tone(notes[n], t, 0.08)
        s += pad_tone(notes[n], t, 0.04)
    mi = int(t / (duration / len(melody_notes))) % len(melody_notes)
    mn = melody_notes[mi]
    beat_t = t % (duration / len(melody_notes))
    env = min(beat_t * 8, 1) * max(0, 1 - beat_t * 1.5)
    s += string_tone(notes[mn], t, env * 0.15)
    fade = min(t / 2, 1) * min((duration - t) / 2, 1)
    samples.append(s * fade * 0.8)
write_wav(os.path.join(base, 'main_theme.wav'), samples)
print('main_theme.wav OK')

# 2. castle_calm.wav - Peaceful
duration = 30
samples = []
chords = [('C3','E3','G3'),('A3','C4','E4'),('F3','A3','C4'),('G3','B3','D4')]
chord_dur = duration / (len(chords) * 2)
for i in range(int(duration * RATE)):
    t = i / RATE
    ci = int(t / chord_dur) % len(chords)
    chord = chords[ci]
    s = 0
    for n in chord:
        s += pad_tone(notes[n], t, 0.06)
    arp_idx = int(t * 2) % 3
    arp_note = chord[arp_idx]
    arp_env = 0.5 + 0.5 * math.sin(2*math.pi*2*t)
    s += math.sin(2*math.pi*notes[arp_note]*2*t) * 0.03 * arp_env
    fade = min(t/2, 1) * min((duration-t)/2, 1)
    samples.append(s * fade * 0.9)
write_wav(os.path.join(base, 'castle_calm.wav'), samples)
print('castle_calm.wav OK')

# 3. great_hall.wav - Regal
duration = 30
samples = []
chords = [('G3','B3','D4'),('C4','E4','G4'),('D3','F#3','A3'),('G3','B3','D4')]
chord_dur = duration / (len(chords)*2)
for i in range(int(duration * RATE)):
    t = i / RATE
    ci = int(t / chord_dur) % len(chords)
    chord = chords[ci]
    s = 0
    for n in chord:
        s += organ_tone(notes[n], t, 0.07)
        s += pad_tone(notes[n], t, 0.04)
    if int(t * 1.5) % 4 == 0:
        mn = chord[0]
        s += math.sin(2*math.pi*notes[mn]*t) * 0.08
    fade = min(t/2,1) * min((duration-t)/2,1)
    samples.append(s * fade * 0.85)
write_wav(os.path.join(base, 'great_hall.wav'), samples)
print('great_hall.wav OK')

# 4. tension.wav - Suspenseful with heartbeat
duration = 30
samples = []
for i in range(int(duration * RATE)):
    t = i / RATE
    s = 0
    s += math.sin(2*math.pi*55*t) * 0.15
    s += math.sin(2*math.pi*55*1.5*t) * 0.08
    pulse = 0.5 + 0.5 * math.sin(2*math.pi*0.8*t)
    s += math.sin(2*math.pi*110*t) * 0.05 * pulse
    s += math.sin(2*math.pi*466*t) * 0.02 * (0.5+0.5*math.sin(2*math.pi*0.3*t))
    beat_period = 0.8
    beat_pos = t % beat_period
    if beat_pos < 0.1:
        s += math.sin(2*math.pi*50*beat_pos) * math.exp(-beat_pos*30) * 0.3
    elif 0.15 < beat_pos < 0.25:
        bp2 = beat_pos - 0.15
        s += math.sin(2*math.pi*60*bp2) * math.exp(-bp2*35) * 0.2
    fade = min(t/2,1) * min((duration-t)/2,1)
    samples.append(s * fade * 0.9)
write_wav(os.path.join(base, 'tension.wav'), samples)
print('tension.wav OK')

# 5. night_mystery.wav - Eerie Am pad
duration = 30
samples = []
for i in range(int(duration * RATE)):
    t = i / RATE
    s = 0
    s += pad_tone(notes['A3'], t, 0.06)
    s += pad_tone(notes['C4'], t, 0.04)
    s += pad_tone(notes['E4'], t, 0.04)
    wander = notes['E5'] + math.sin(2*math.pi*0.1*t) * 50
    s += math.sin(2*math.pi*wander*t) * 0.02 * (0.5+0.5*math.sin(2*math.pi*0.2*t))
    wind = random.uniform(-1,1) * 0.02 * (0.5+0.5*math.sin(2*math.pi*0.15*t))
    s += wind
    fade = min(t/3,1) * min((duration-t)/3,1)
    samples.append(s * fade * 0.8)
write_wav(os.path.join(base, 'night_mystery.wav'), samples)
print('night_mystery.wav OK')

# 6. sad.wav - Melancholic Em
duration = 30
samples = []
chords_sad = [('E3','G3','B3'),('C3','E3','G3'),('G3','B3','D4'),('D3','F#3','A3')]
chord_dur = duration / (len(chords_sad)*2)
melody_sad = ['B4','A4','G4','E4','G4','A4','B4','A4']
for i in range(int(duration * RATE)):
    t = i / RATE
    ci = int(t / chord_dur) % len(chords_sad)
    chord = chords_sad[ci]
    s = 0
    for n in chord:
        s += pad_tone(notes[n], t, 0.06)
    mi = int(t / (duration/len(melody_sad))) % len(melody_sad)
    mn = melody_sad[mi]
    mel_t = t % (duration/len(melody_sad))
    env = math.exp(-mel_t * 0.8) * min(mel_t * 10, 1)
    s += string_tone(notes[mn], t, env * 0.1)
    fade = min(t/3,1) * min((duration-t)/3,1)
    samples.append(s * fade * 0.8)
write_wav(os.path.join(base, 'sad.wav'), samples)
print('sad.wav OK')

# 7. battle_prepare.wav - War drums + brass
duration = 30
samples = []
for i in range(int(duration * RATE)):
    t = i / RATE
    s = 0
    drum_period = 0.5
    dp = t % drum_period
    if dp < 0.08:
        s += math.sin(2*math.pi*80*dp) * math.exp(-dp*25) * 0.5
    if 0.25 < dp < 0.33:
        dp2 = dp - 0.25
        s += math.sin(2*math.pi*100*dp2) * math.exp(-dp2*30) * 0.35
    s += organ_tone(notes['D3'], t, 0.08)
    s += organ_tone(notes['A3'], t, 0.05)
    intensity = min(t / duration * 1.5, 1)
    s += math.sin(2*math.pi*notes['D4']*t) * 0.03 * intensity
    fade = min(t/1,1) * min((duration-t)/2,1)
    samples.append(s * fade * intensity * 0.8)
write_wav(os.path.join(base, 'battle_prepare.wav'), samples)
print('battle_prepare.wav OK')

# 8. victory.wav - Triumphant C major
duration = 30
samples = []
chords_v = [('C4','E4','G4'),('F3','A3','C4'),('G3','B3','D4'),('C4','E4','G4')]
chord_dur = duration / (len(chords_v)*2)
for i in range(int(duration * RATE)):
    t = i / RATE
    ci = int(t / chord_dur) % len(chords_v)
    chord = chords_v[ci]
    s = 0
    for n in chord:
        s += organ_tone(notes[n], t, 0.08)
        s += pad_tone(notes[n], t, 0.05)
    fanfare_t = t % chord_dur
    if fanfare_t < 0.3:
        s += math.sin(2*math.pi*notes['C5']*t) * math.exp(-fanfare_t*5) * 0.1
    fade = min(t/1,1) * min((duration-t)/2,1)
    samples.append(s * fade * 0.85)
write_wav(os.path.join(base, 'victory.wav'), samples)
print('victory.wav OK')

print('\nAll 8 music tracks regenerated!')
