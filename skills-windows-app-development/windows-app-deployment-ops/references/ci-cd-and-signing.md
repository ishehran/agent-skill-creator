# CI CD And Signing

Core release pipeline requirements:

1. Build reproducible artifacts from tagged source.
2. Run automated tests and static checks.
3. Sign binaries/installers with managed certificate flow.
4. Store checksums and provenance metadata.
5. Promote exact same artifact across release rings.

Never rebuild separately for later release stages.

