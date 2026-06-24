# Snow Crash

> A security project — an introduction to cyber security.

## About

Snow Crash is a wargame-style project made of a series of challenges, each one locked behind a level. The goal is to escalate from one level to the next by finding the password to the corresponding `flag` account, then running `getflag` to reveal the token that grants access to the next level.

Each level teaches a different cyber security concept — file permissions, command injection, reverse engineering, cryptography, environment manipulation, and more.

## How it works

The project runs on a 64-bit virtual machine booted from the provided ISO. Once started, connect over SSH:

```sh
ssh level00@<VM_IP> -p 4242
```

Starting credentials are `level00:level00`. From there, each level follows the same pattern:

1. Explore the level's environment and find the next password.
2. Switch to the matching flag account:
   ```sh
   su flagXX   # XX = current level number
   ```
3. Run `getflag` to obtain the token.
4. Use that token to log into the next level (`levelXX+1`).

## Repository structure

Each level has its own folder containing the flag and the resources used to solve it.

```
.
├── level00/
│   ├── flag
│   └── resources/
├── level01/
│   ├── flag
│   └── resources/
├── ...
└── level09/
    ├── flag
    └── resources/
```

- **`flag`** — the token retrieved via `getflag` (may be empty for some levels).
- **`resources/`** — scripts, notes, and any files used to reach the solution.

## Levels

**Mandatory:** `level00` → `level09`

**Bonus:** `level10` → `level14`

## Notes

- No binary files are included in this repository.
- Files from the project's ISO are not committed; they are downloaded during evaluation if needed.
- Brute forcing the SSH flags is not permitted.
