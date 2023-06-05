[
{
  "elements": [
    {
      "keyword": "Background",
      "location": "BrainBucket/BDDBehave/logintests/login.feature:3",
      "name": "",
      "steps": [
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:4",
          "name": "User launch login page",
          "step_type": "given"
        }
      ],
      "type": "background"
    },
    {
      "keyword": "Scenario",
      "location": "BrainBucket/BDDBehave/logintests/login.feature:7",
      "name": "a user can login using correct email and password",
      "status": "failed",
      "steps": [
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:4",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:22"
          },
          "name": "User launch login page",
          "result": {
            "duration": 4.607071161270142,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:8",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:28"
          },
          "name": "User is not logged in",
          "result": {
            "duration": 0.1518568992614746,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:9",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:42"
          },
          "name": "user enters email and password",
          "result": {
            "duration": 0.008011817932128906,
            "error_message": [
              "Traceback (most recent call last):",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\model.py\", line 1329, in run",
              "    match.run(runner.context)",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\matchers.py\", line 98, in run",
              "    self.func(context, *args, **kwargs)",
              "  File \"BrainBucket\\BDDBehave\\logintests\\steps\\loginsteps.py\", line 45, in enter_email_and_password",
              "    configs = context.configs",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\runner.py\", line 321, in __getattr__",
              "    raise AttributeError(msg)",
              "AttributeError: 'Context' object has no attribute 'configs'"
            ],
            "status": "failed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:10",
          "name": "User clicks Login button",
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:11",
          "name": "The user's profile page will be launched",
          "step_type": "then"
        }
      ],
      "tags": [
        "positive"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "BrainBucket/BDDBehave/logintests/login.feature:14",
      "name": "User can't login without entering password",
      "status": "failed",
      "steps": [
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:4",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:22"
          },
          "name": "User launch login page",
          "result": {
            "duration": 4.438540935516357,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:15",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:28"
          },
          "name": "User is not logged in",
          "result": {
            "duration": 0.14403629302978516,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:16",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:65"
          },
          "name": "User enters email",
          "result": {
            "duration": 0.0,
            "error_message": [
              "Traceback (most recent call last):",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\model.py\", line 1329, in run",
              "    match.run(runner.context)",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\matchers.py\", line 98, in run",
              "    self.func(context, *args, **kwargs)",
              "  File \"BrainBucket\\BDDBehave\\logintests\\steps\\loginsteps.py\", line 68, in enter_email",
              "    login_page.enter_email(context.configs.get_user1_email())",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\runner.py\", line 321, in __getattr__",
              "    raise AttributeError(msg)",
              "AttributeError: 'Context' object has no attribute 'configs'"
            ],
            "status": "failed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:17",
          "name": "User clicks Login button",
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:18",
          "name": "warning is shown 'No match for E-Mail Address and/or Password'",
          "step_type": "then"
        }
      ],
      "tags": [
        "negative",
        "enter_email"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "BrainBucket/BDDBehave/logintests/login.feature:21",
      "name": "User can't login without entering email",
      "status": "failed",
      "steps": [
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:4",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:22"
          },
          "name": "User launch login page",
          "result": {
            "duration": 3.9090635776519775,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:22",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:28"
          },
          "name": "user is not logged in",
          "result": {
            "duration": 0.15230655670166016,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:23",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:71"
          },
          "name": "user enters password",
          "result": {
            "duration": 0.0,
            "error_message": [
              "Traceback (most recent call last):",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\model.py\", line 1329, in run",
              "    match.run(runner.context)",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\matchers.py\", line 98, in run",
              "    self.func(context, *args, **kwargs)",
              "  File \"BrainBucket\\BDDBehave\\logintests\\steps\\loginsteps.py\", line 74, in enter_password",
              "    login_page.enter_password(context.configs.get_user1_password())",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\runner.py\", line 321, in __getattr__",
              "    raise AttributeError(msg)",
              "AttributeError: 'Context' object has no attribute 'configs'"
            ],
            "status": "failed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:24",
          "name": "user clicks Login button",
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:25",
          "name": "warning is shown 'No match for E-Mail Address and/or Password'",
          "step_type": "then"
        }
      ],
      "tags": [
        "negative",
        "skip",
        "enter_password"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "BrainBucket/BDDBehave/logintests/login.feature:28",
      "name": "User on the login page can reset password with correct email",
      "status": "failed",
      "steps": [
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:4",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:22"
          },
          "name": "User launch login page",
          "result": {
            "duration": 4.564150810241699,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "Given",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:29",
          "match": {
            "arguments": [],
            "location": "BrainBucket/BDDBehave/logintests/steps/loginsteps.py:36"
          },
          "name": "user clicks 'Forgotten Password'",
          "result": {
            "duration": 0.008391141891479492,
            "error_message": [
              "Traceback (most recent call last):",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\model.py\", line 1329, in run",
              "    match.run(runner.context)",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\matchers.py\", line 98, in run",
              "    self.func(context, *args, **kwargs)",
              "  File \"BrainBucket\\BDDBehave\\logintests\\steps\\loginsteps.py\", line 38, in click_forgotten_btn",
              "    login_page = context.login_page",
              "  File \"C:\\Users\\Volodymyr\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\behave\\runner.py\", line 321, in __getattr__",
              "    raise AttributeError(msg)",
              "AttributeError: 'Context' object has no attribute 'login_page'"
            ],
            "status": "failed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:30",
          "name": "user enters email",
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:31",
          "name": "user clicks Continue button",
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "BrainBucket/BDDBehave/logintests/login.feature:32",
          "name": "confirmation message is shown 'An email with a confirmation link has been sent your email address'",
          "step_type": "then"
        }
      ],
      "tags": [
        "positive",
        "password_reset"
      ],
      "type": "scenario"
    }
  ],
  "keyword": "Feature",
  "location": "BrainBucket/BDDBehave/logintests/login.feature:2",
  "name": "Login functionality",
  "status": "failed",
  "tags": [
    "wip"
  ]
}
]
