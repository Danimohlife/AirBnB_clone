t are namespace and name?

They’re both inputs used to generate a UUID deterministically — meaning:

    Same namespace + same name = always same UUID
    Different name or different namespace = different UUID

This is helpful when:

    You want to generate IDs based on human-readable input (like URLs or usernames)

    But don’t want to store the IDs — just regenerate them when neede
