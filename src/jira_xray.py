import requests


def create_jira_test_issue(
    base_url: str,
    email: str,
    api_token: str,
    project_key: str,
    summary: str,
    description: str,
    issue_type: str = "Test",
) -> dict:
    """
    Create a Test issue in Jira/Xray.

    Parameters
    ----------
    base_url : str
        Example: https://yourcompany.atlassian.net
    email : str
        Jira account email.
    api_token : str
        Atlassian API token.
    project_key : str
        Example: QA
    summary : str
        Issue summary/title.
    description : str
        Detailed test case content.
    issue_type : str
        Usually "Test" when Xray is installed.

    Returns
    -------
    dict
        Jira API response.
    """

    url = f"{base_url.rstrip('/')}/rest/api/3/issue"

    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": description,
            "issuetype": {"name": issue_type},
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    response = requests.post(
        url,
        json=payload,
        auth=(email, api_token),
        headers=headers,
        timeout=60,
    )

    response.raise_for_status()
    return response.json()


def create_multiple_test_issues(
    base_url: str,
    email: str,
    api_token: str,
    project_key: str,
    test_cases: list[str],
) -> list[str]:
    """
    Create multiple Jira/Xray Test issues.

    Parameters
    ----------
    test_cases : list[str]
        Each item is treated as one test case description.

    Returns
    -------
    list[str]
        Created issue keys, e.g. ["QA-101", "QA-102"]
    """

    created_keys = []

    for index, test_case in enumerate(test_cases, start=1):
        response = create_jira_test_issue(
            base_url=base_url,
            email=email,
            api_token=api_token,
            project_key=project_key,
            summary=f"AI Generated Test Case {index}",
            description=test_case,
        )

        if "key" in response:
            created_keys.append(response["key"])

    return created_keys