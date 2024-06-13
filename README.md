
# ChatGPT 2024 - Assistant with Project Usage

![Last Commit](https://img.shields.io/github/last-commit/Siphon880gh/chatgpt-2024/main)
<a target="_blank" href="https://github.com/Siphon880gh" rel="nofollow"><img src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" alt="Github" data-canonical-src="https://img.shields.io/badge/GitHub--blue?style=social&logo=GitHub" style="max-width:8.5ch;"></a>
<a target="_blank" href="https://www.linkedin.com/in/weng-fung/" rel="nofollow"><img src="https://camo.githubusercontent.com/0f56393c2fe76a2cd803ead7e5508f916eb5f1e62358226112e98f7e933301d7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c696e6b6564496e2d626c75653f7374796c653d666c6174266c6f676f3d6c696e6b6564696e266c6162656c436f6c6f723d626c7565" alt="Linked-In" data-canonical-src="https://img.shields.io/badge/LinkedIn-blue?style=flat&amp;logo=linkedin&amp;labelColor=blue" style="max-width:10ch;"></a>
<a target="_blank" href="https://www.youtube.com/user/Siphon880yt/" rel="nofollow"><img src="https://camo.githubusercontent.com/0bf5ba8ac9f286f95b2a2e86aee46371e0ac03d38b64ee2b78b9b1490df38458/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f596f75747562652d7265643f7374796c653d666c6174266c6f676f3d796f7574756265266c6162656c436f6c6f723d726564" alt="Youtube" data-canonical-src="https://img.shields.io/badge/Youtube-red?style=flat&amp;logo=youtube&amp;labelColor=red" style="max-width:10ch;"></a>

## :page_facing_up: Description:
By Weng Fei Fung. This is an update to my ChatGPT Boilerplate now leveraging the new 2024 features. Associate your OpenAI calls to a project API key so you can view usage at project level (previously OpenAI only offered User API Keys not distinguishing between projects). In addition, the code now leverages assistants, creating your own GPTs to use on the backend API calls.

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

Grab your API keys and ID's:
- Organization ID: https://platform.openai.com/settings/organization/general
- Project ID: https://platform.openai.com/settings/proj_vxAxeUNXy9GofbFJ8qJWDFjR/general
- API Key: https://platform.openai.com/api-keys
- Assistant ID: https://platform.openai.com/assistants

## :runner: Usage:
Run directly `python script.py`