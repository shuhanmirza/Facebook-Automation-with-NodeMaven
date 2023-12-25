# Facebook-Automation-with-NodeMaven

So, you want to build a bot for Facebook. You are in the right repo. This repo has some common 
functions needed to build a Facebook bot. I used NodeMaven's Residential Proxies to bypass Facebook's bot detection 
mechanism. By the end of this guide, you'll have a script that effortlessly logs into Facebook, 
performs the workflow, benefiting from the diverse residential IP addresses of NodeMaven.

## Prerequisites

- Install Python3
- Setup virtualenv
- Install required packages

```console
your_pc$ virtualenv -p /usr/bin/python3 venv
```

```console
your_pc$ source venv/bin/activate
```

```console
(venv)your_pc$ pip install -r requirements.txt
```

- Have Google Chrome installed
- Rename `env_sample.json` to `env.json` and configure it with your Facebook username and password, and Proxy username and password
```json
{
  "username": "john.doe",
  "password": "john1234",
  "proxy_username": "john-doe-country-lt",
  "proxy_password": "john1234"
}
```

## Workflow
Edit the `workflow` function to define your workflow.

```python
def workflow():
    # Define your workflow here!

    target_post = 'https://www.facebook.com/nixcraft/posts/pfbid02UL8ijMgqMgDJ6aqiu6bHEaFmaFG519Nf58oNXcUQrYvi84tgUb5idhQnTpEDeFAHl'
    browser = get_browser()
    facebook_login(browser)
    facebook_goto_post(browser=browser, target_post=target_post)
    facebook_haha(browser)
```
In this sample workflow, the bot goes to the target post and reacts with _Haha_.

## Running

```console
(venv)your_pc$ python main.py
```

## NodeMaven's Residential Proxies:

To get started, register on the NodeMaven platform using [this link](https://go.nodemaven.com/proxies17), choose the trial on your personal account, and apply the coupon code `PLUS2` during the trial setup to receive **2GB** of traffic for free.

## Conclusion:

By integrating NodeMaven's Residential Proxies, your bot will perform the workflow without being detected. 
Using the common functions in the repo you can easily build your required workflows. Open Issues and PRs if you want to see 
more functionalities.
