DATA_PATH = "data/survey_results_public.csv"
CKPT_PATH = "random_forest_pipeline.joblib"

FEATURE_LIST = ["RemoteWork", "EdLevel", "YearsCodePro", "DevType", "LanguageHaveWorkedWith", "PlatformHaveWorkedWith", 
"ToolsTechHaveWorkedWith",
"Country", "Age", "ConvertedCompYearly"]

LANGUAGE = ['JavaScript', 'HTML/CSS', 'SQL',
       'TypeScript', 'Python', 'Bash/Shell (all shells)', 'Java', 'C#', 'PHP', 'Go', 'C++',
       'PowerShell']
PLATFORM = ['Amozon Web Services(AWS)', 'Microsoft Azure', 'Google Cloud', 'Cloudflare', 'Oracle Cloud Infrastructure (OCI)', 'Digital Ocean']
TOOLS = ['Docker', 'npm', 'Homebrew', 'Yarn', 'Kubernetes', 'Ansible' , 'Grandle', 'Make', 'Pip']
TYPES = ['Developer, full-stack', 'Developer, back-end', 'Developer, front-end',
       'DevOps specialist', 'Cloud infrastructure engineer',
       'Developer, desktop or enterprise applications', 'Developer, mobile',
       'Database administrator', 'Engineering manager', 'System administrator',
       'Project manager', 'Developer, QA or test',
       'Developer, embedded applications or devices', 'Designer',
       'Data scientist or machine learning specialist',
       'Engineer, site reliability', 'Data engineer', 'Developer, AI']
COLUMNS = ['RemoteWork', 'EdLevel', 'YearsCodePro', 'Country', 'Age',
       'Developer, full-stack', 'Developer, back-end', 'Developer, front-end',
       'DevOps specialist', 'Cloud infrastructure engineer',
       'Developer, desktop or enterprise applications', 'Developer, mobile',
       'Database administrator', 'Engineering manager', 'System administrator',
       'Project manager', 'Developer, QA or test',
       'Developer, embedded applications or devices', 'Designer',
       'Data scientist or machine learning specialist',
       'Engineer, site reliability', 'Data engineer', 'Developer, AI', 'JavaScript', 'HTML/CSS', 'SQL',
       'TypeScript', 'Python', 'Bash/Shell (all shells)', 'Java', 'C#', 'PHP', 'Go', 'C++',
       'PowerShell', 'Docker', 'npm', 'Homebrew', 'Yarn', 'Kubernetes', 'Ansible' , 'Grandle', 'Make', 'Pip', "Amazon Web Services (AWS)", 'Microsoft Azure', 'Google Cloud', 'Cloudflare', 'Oracle Cloud Infrastructure (OCI)', 'Digital Ocean']
COUNTRY = ['United Kingdom of Great Britain and Northern Ireland',
       'United States of America', 'Other', 'Austria', 'Italy', 'Canada',
       'Germany', 'Poland', 'Israel', 'Netherlands', 'France', 'Spain',
       'Turkey', 'Sweden', 'India', 'Belgium', 'Brazil', 'Switzerland',
       'Australia', 'Portugal', 'Russian Federation', 'Mexico']