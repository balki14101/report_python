personalDetails = '''{
    "PersonId": "P1",
    "Name": "Rohit",
    "Age": 20    
}
'''
response = '''
{
    "PersonId": "P1",
    "Name": "Rohit",
    "CompSurveyID": "CS001",
    "SurveyName": "Mental Health",
    "Date" : "30/01/2024",
    "Question": [
        {
            "QuestionID": "QN001",
            "SurveyQuestionNo": "1",
            "Score": 1,
            "Layer": "L1",
            "Domain": "Anxiety",
            "Subdomain": "Worrying",
            "Section": "Section1"
        },
        {
            "QuestionID": "QN002",
            "SurveyQuestionNo": "2",
            "Score": 1,
            "Layer": "L1",
            "Domain": "Anxiety",
            "Subdomain": "Muscular Tension",
            "Section": "Section1"
        },
        {
            "QuestionID": "QN003",
            "SurveyQuestionNo": "2",
            "Score": 1,
            "Layer": "L1",
            "Domain": "Depression",
            "Subdomain": "Self Confidence",
            "Section": "Section1"
        },
        {
            "QuestionID": "QN004",
            "SurveyQuestionNo": "2",
            "Score": 0,
            "Layer": "L1",
            "Domain": "Depression",
            "Subdomain": "Self Confidence",
            "Section": "Section1"
        }
    ]
}
'''

recommendation = '''
{
    "scale": [
        {
            "LevelName": "Anxiety",
            "Range": "0%",
            "Rating": "nothing"
        },
        {
            "LevelName": "Anxiety",
            "Range": "0-25%",
            "Rating": "normal"
        },
        {
            "LevelName": "Anxiety",
            "Range": "50-75%",
            "Rating": "moderate"
        },
        {
            "LevelName": "Anxiety",
            "Range": "75-100%",
            "Rating": "severe"
        },
        {
            "LevelName": "Muscular Tension",
            "Range": ">63%",
            "Rating": "high"
        },
        {
            "LevelName": "Self Confidence",
            "Range": ">63%",
            "Rating": "high"
        }
    ]
}
'''

static='''{
    "header_title": "Survey Report",
    "about_title": "About this Survey",
    "about_survey_content1": "A psychology survey is a research tool used to gather information about various psychological phenomena, attitudes, behaviors, or experiences of individuals. These surveys are designed to explore a wide range of topics within psychology, including personality traits, mental health issues, cognitive processes, social interactions, and more.",
    "about_survey_content2":"Typically, psychology surveys consist of a series of rating scales or open-ended questions. The questions are often crafted to address specific research objectives and hypotheses, and they may cover various aspects of the human mind and behavior.",
    "accurate_title": "Is this survey accurate?",
    "accurate_content": "Claiming 100% accuracy for any survey is unrealistic. While surveys aim for accuracy, inherent limitations such as response bias or sampling errors prevent absolute certainty. Acknowledging these limitations fosters transparency and credibility in research. Thus, while striving for accuracy, claiming 100% accuracy is not feasible.",
    "score": "Score",
    "level": "Level",
    "range": "Range",
    "analysis": "Analysis",
    "domainAnalysis": "Domain Analysis",
    "subdomainAnalysis": "Sub-Domain Analysis",
    "recommendation": "Recommendation"
    
}
'''

styles='''
{
    "font": {
        "arial": "Arial"
    },
    "weight": {
        "bold": "B"
    },
    "fontsize": {
        "small": 10,
        "normal": 12,
        "medium": 14,
        "large": 16
    },
    "width": {
        "zero": 0,
        "small": 40,
        "large": 200
    },
    "height": {
        "medium": 10,
        "large": 40,
        "small": 5
    },
    "align": {
        "center": "C"
    }
}
'''

images='''
{
    "logo": {
        "source": "logo.png",
        "x": 10,
        "y": 10,
        "w": 30
    },
    "domain": {},
    "subdomain": {}
}
   '''






page_style='''
{
    
    "header": {
        "fontstyle": "Arial",
        "weight": "B",
        "fontsize": 14
    },

    "headerCell": {
        "w": 200,
        "h": 40,
        "text": "Survey Report",
        "border": 0,
        "line": 2,
        "align": "C"
    },

    "content":{
    "fontstyle": "Arial",
        "weight": "B",
        "fontsize": 12
    },

    "contentCell":{
    "w": 40,
        "h": 10,
        "border": 0,
        "line": 2
    },

    "logo":{
    "source":"logo.png",
    "x":10,
    "y":10,
    "w":30
    },

    "line":{
    "x1":10,
    "y1":40,
    "x2":200,
    "y2":40
    },
    "multicell":{
    "w":0,
    "h":5
    }
}

'''




