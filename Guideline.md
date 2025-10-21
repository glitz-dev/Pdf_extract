# Adding to Huggingface

1. Check Current status -> git remote -v
2. To remove an exisitng HF Repo -> git remote remove hf
3. To add Files to HF Repo -> git remote add hf https://huggingface.co/spaces/Username/SpaceName
4. Then commit using -> git push hf main OR git push hf main --force

#### Not permitting to add files to HF, generate new token with write permission

1. Go to https://huggingface.co/settings/tokens
2. Click **New token**
3. Name it something like: hf-cli
4. Set **Role = Write**
5. Copy the generated token.
6. logout and login in hf,
        - huggingface-cli logout (deprecated) / hf auth logout
        - huggingface-cli login (deprecated) / hf auth login
        - paste key + enter / $env:HF_TOKEN = "token-no"
7. confirm identity
        - huggingface-cli whoami (deprecated)/ hf auth whoami
8. try to push again
        - git push hf main --force      


git remote set-url origin https://<YOUR_USERNAME>:<YOUR_TOKEN>@huggingface.co/spaces/<YOUR_USERNAME>/<YOUR_REPO>.git

To check root folder in Repo ->  git rev-parse --show-toplevel

To fetch remote branches -> git fetch hf
To check remote branches -> git branch -r
Switch to main branch -> git checkout main

