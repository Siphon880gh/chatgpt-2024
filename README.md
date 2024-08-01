
# ChatGPT 2024 - Assistant with Project Usage

![Last Commit](https://img.shields.io/github/last-commit/Siphon880gh/chatgpt-2024/main)
<a target="_blank" href="https://github.com/Siphon880gh" rel="nofollow"><img src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" alt="Github" data-canonical-src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" style="max-width:8.5ch;"></a>
<a target="_blank" href="https://www.linkedin.com/in/weng-fung/" rel="nofollow"><img src="https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue" alt="Linked-In" data-canonical-src="https://img.shields.io/badge/LinkedIn-blue?style=flat&amp;logo=linkedin&amp;labelColor=blue" style="max-width:10ch;"></a>
<a target="_blank" href="https://www.youtube.com/@WayneTeachesCode/" rel="nofollow"><img src="https://img.shields.io/badge/Youtube-red?style=flat&logo=youtube&labelColor=red" alt="Youtube" data-canonical-src="https://img.shields.io/badge/Youtube-red?style=flat&amp;logo=youtube&amp;labelColor=red" style="max-width:10ch;"></a>

## :page_facing_up: Description:
By Weng Fei Fung. Updated ChatGPT boilerplate leveraging the 2024 features. Associate your OpenAI calls to a project API key so you can view usage at project level (previously OpenAI only offered User API Keys not distinguishing between projects). In addition, the code now leverages assistants, creating your own GPTs to use on the backend API calls.

## :open_file_folder: Table of Contents:
---
- [Description](#page_facing_up-description)
- [Installation](#minidisc-installation)
- [Usage](#runner-usage)

## :minidisc: Installation:
Have python installed. Install openai 1.34.0 (`pip install openai`)

Create `.env` file with the corresponding keys and values:
```
OPENAI_API_KEY=sk-...
OPENAI_ORG_ID=org-...
OPENAI_PROJ_ID=proj_...
OPENAI_ASSISTANT_TRANSLATOR=asst_...
```

Create your assistant at
https://platform.openai.com/docs/assistants/overview?context=with-streaming

Please note these assistants are not the same as the GPTs you create in their chat interface.

Grab your API keys and ID's:
- Organization ID: https://platform.openai.com/settings/organization/general
- Project ID: https://platform.openai.com/settings/proj_vxAxeUNXy9GofbFJ8qJWDFjR/general
- API Key: https://platform.openai.com/api-keys
- Assistant ID: https://platform.openai.com/assistants

## :runner: Usage:
Run directly `python script.py`
