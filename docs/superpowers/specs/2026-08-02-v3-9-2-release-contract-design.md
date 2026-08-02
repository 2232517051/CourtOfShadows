# 3.9.2 Release Contract and Distribution Cleanup Design

**Date:** 2026-08-02  
**Status:** Approved (方案 A)  
**Target:** `codex/v3-9-2-rc`

## Goal

Turn the already regression-tested 3.9.2 branch into uploadable Windows and Android distributions. The release must describe the game as it exists, carry reproducible Android metadata, omit internal and unused payloads, retain old-save compatibility, and gain automated gates that catch the same class of release drift.

## Player-facing facts

The current source proves the following claims and no stronger ones:

- The product version is 3.9.2.
- The main story has five chapters.
- The main ending catalog contains exactly nine endings.
- “父与子” is a hidden epilogue and is not a tenth catalog ending.
- The Southern side story records five separate outcomes and does not change the nine-ending main catalog.
- New Game+ carries forward 20% of Power, Wealth, and Intrigue. It does not unlock a separate set of story content.
- The six main values are Power, Wealth, Faith, Loyalty, Reputation, and Intrigue.
- The repository does not contain reliable playtime evidence. Current release copy must not promise a number of hours.
- Windows and Android packages exist. Store availability must not be inferred from that fact.

Historical changelog entries may retain the ending count and terminology that were true for their own versions. Only current release material is normalized.

## Copy direction

All new Chinese game and store copy uses nearby Chinese passages from both *The Life and Suffering of Prince Jerian* and *The Life and Suffering of Sir Brante* as Few-shot examples, as required by `writing-game-copy`.

The selected examples are:

- `jerian_zh.txt:37-45` and `:88-97`: direct second-person framing, a concrete question, and consequences stated without promotional superlatives.
- `brante_zh.txt:4823-4830` and `:4844-4851`: choices close some paths and open others; failure and cost are described plainly.

The release copy will therefore state the initial situation, the constraints on the player, and the actual systems. It will not use an unverifiable duration, “every choice changes history”, “unlock new content”, or an unavailable store status.

Required current-copy changes:

- `game/options.rpy`: replace the stale About body and v3.2 footer.
- `game/effects.rpy`: update the privacy version/date and make the rating prompt platform-neutral; its button must describe its real close-only action.
- `game/pv.rpy`: label the five shown endings as a partial preview, state the nine-ending total, and replace the stale store-status line with the factual platform line `PC · Android`.
- `README.txt`: become a player installation/readme file, not source-project instructions.
- `DESCRIPTION.txt`, `DEVELOPER_NOTE.txt`, and `store_assets/taptap_description.txt`: use the current nine-ending, six-value, and New Game+ facts; remove playtime claims.
- `Tools/make_trailer.py`: update the derived store-trailer title card from eight to nine main paths, then regenerate the trailer from existing images and music if the toolchain is available.

## Distribution classification

Exclusions are packaging rules only. Source and working assets stay in the repository.

Rules must precede the general `game/**.rpyc`, image, and audio inclusion rules because Ren'Py classification is first-match-wins.

Exclude from player distributions:

- `game/test_game.rpyc`.
- `game/audio/music/*_alt.mp3`.
- `game/audio/music/test3.wav`.
- `game/audio/narration/test_guy.mp3` and `game/audio/narration/voice_test/**`.
- `game/images/hd/**`, `game/images/backup_sd/**`, and `game/images/webp_backup/**`.
- `store_assets/**`, `tests/**`, `docs/**`, and `Tools/**`.
- The explicit root marketing images, mockups, reports, project rules, old announcements, store-only copy, changelog documents, and progress JSON files found in the current package.

Keep one corrected `README.txt` in the Windows distribution. Do not include it in Android assets. Keep Android icon and presplash inputs available to the build process.

Do not delete or relocate `old-game/*.rpyc`. Ren'Py consumes those files during compilation to retain historical script nodes. The source directory must remain complete, while the resulting Windows/APK archives must continue to omit the directory itself.

The 22 dynamically risky zero-reference UI images are outside this 3.9.2 cleanup. They remain packaged until a dedicated runtime render sweep proves each exact path removable.

## Android metadata

Synchronize source metadata to the already verified build contract:

- Package: `com.xiaoyiai.courtofshadows`.
- Version name: `3.9.2`.
- Target/compile SDK expectation: 36.
- `numeric_version` is a lower bound for Ren'Py's timestamp-based version code. Set it to at least the previously built code `1785596475`; the final manifest must be strictly greater than that value.
- Orientation remains landscape.
- Final APK must remain signed by the same certificate as 3.9.1 and pass zipalign verification.

## Automated gates

### Source release contract

Add `Tools/test_release_contract.py` and make it fail on:

- disagreement between `config.version` and `android.json.version`;
- disagreement between package or target SDK fields;
- anything other than the nine-key main ending catalog;
- stale current-copy phrases such as five endings, a numeric playtime, v3.2/v3.1, “New Game+ unlocks new content”, or “即将登陆 TapTap · Steam”;
- missing high-confidence packaging exclusions or exclusions ordered after generic inclusions;
- missing `old-game` compatibility inputs.

Historical changelogs and archived announcements are not current-copy inputs and are excluded from text assertions.

### Render checks

Add a focused Ren'Py test that truly renders the About and privacy screens after the new interpolation/text changes. Capture screenshots and inspect them at original resolution.

### Built-distribution contract

Add `Tools/verify_distributions.py` to validate:

- ZIP/APK integrity;
- required executable and production RPYC presence;
- forbidden internal/test/store/backup payload absence, including Android `assets/x-*` equivalents;
- `old-game/` absence from archives without touching the source directory;
- APK package, version name, version code, target SDK, orientation, zipalignment, and signing certificate;
- final archive sizes against a post-cleanup baseline with modest headroom.

## Execution order

1. Add the failing source release-contract test.
2. Correct current copy and Android metadata until it passes.
3. Add the failing classification assertions and implement explicit exclusions.
4. Run the complete source regression suite while `game/test_game.rpy` is still available in source.
5. Add the distribution verifier and demonstrate it fails against the current bloated packages.
6. Rebuild Windows and Android distributions.
7. Verify package contents, APK metadata/signature/alignment, Windows launch, and real old-save loading.
8. Render and inspect About/privacy. Regenerate and inspect the existing store trailer if its local toolchain succeeds.

## Asset decision

- **Art:** no new art required. Existing promotional images and in-game art are reused; source promotional images are merely excluded from player archives.
- **Music:** no new music required. Existing OST is reused. Thirty alternate MP3 masters remain in the repository but leave player archives.
- **Sound effects:** no new sound effects required. Test voice/audio files leave player archives.
- **Animation/video:** no new animation source is required. The existing store trailer may be re-rendered from current images and OST; this is a derived-asset refresh, not a new asset request.

