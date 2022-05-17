# vigenere-cipher

It requires two files: a key file and a plan file ready to be encrypted.

## Prepare Commit Msg

To have a more convenient management each branch will have a name structured as follows:
[brench type]/[branch name in uppercase]

### Usage

Copy the prepare-msg-msg in .git/hooks/

```bash
cp prepare-commit-msg .git/hooks/
```

Make it executable

```bash
chmod +x .git/hooks/prepare-commit-msg
```

### Type

The type of the brench can be:

**feature**: an addition to the program (develop -> develop)
**fix**: a bug fix (develop-> develop and release -> release & develop)
**hotfix**: a fix to a blocking bug (main-> main & release)

### Name

The branch name must be one word and uppercase and must simply describe what you are working on.
[eg. FILE, WEBSOCKET, HTTP, ...]
