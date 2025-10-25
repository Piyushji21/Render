# 🚀 MaxLikes API - Complete Vercel Deployment Tutorial

## ✅ What I Fixed

Your deployment was failing due to these 3 critical issues:

1. **Missing `token_ind.json` file** - Added with 5,497 real tokens
2. **File path errors** - Fixed `app.py` to work with Vercel's serverless structure
3. **Outdated config** - Removed deprecated environment variable format from `vercel.json`

---

## 📋 Step-by-Step Deployment Guide

### Step 1: Push Your Code to Git

First, make sure all your files are in a Git repository (GitHub, GitLab, or Bitbucket):

```bash
# If you haven't initialized git yet
git init
git add .
git commit -m "Fixed Vercel deployment issues"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Vercel

1. **Go to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Click **"Sign Up"** or **"Login"** (use GitHub for easier integration)

2. **Import Your Project**
   - Click **"New Project"**
   - Select **"Import Git Repository"**
   - Choose your repository from the list
   - Click **"Import"**

3. **Configure Project Settings**
   - **Project Name**: Choose any name (e.g., `maxlikes-api`)
   - **Framework Preset**: Leave as "Other"
   - **Root Directory**: Click **"Edit"** and select the **`vercel`** folder
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty
   - Click **"Deploy"**

### Step 3: Set Environment Variables (CRITICAL!)

After the first deployment, it will fail because environment variables are missing. Here's how to add them:

1. Go to your project dashboard in Vercel
2. Click **"Settings"** (top navigation)
3. Click **"Environment Variables"** (left sidebar)
4. Add these two variables:

#### Variable 1: SECRET_KEY
```
Name: SECRET_KEY
Value: (Generate using the command below)
Environment: Production, Preview, Development (select all)
```

**Generate your SECRET_KEY:**
```bash
python -c 'import os; print(os.urandom(24).hex())'
```
Example output: `a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4`

Copy this value and paste it as the SECRET_KEY value.

#### Variable 2: ADMIN_PASSWORD
```
Name: ADMIN_PASSWORD
Value: thethestar (or your custom password)
Environment: Production, Preview, Development (select all)
```

4. Click **"Save"** for each variable

### Step 4: Redeploy

After adding environment variables:

1. Go to **"Deployments"** tab
2. Click on the three dots **"⋮"** next to the latest deployment
3. Click **"Redeploy"**
4. Wait for deployment to complete (usually 30-60 seconds)

### Step 5: Test Your Deployment

Once deployed successfully, you'll get a URL like:
```
https://your-project-name.vercel.app
```

**Test the endpoints:**

1. **Homepage (requires login)**
   ```
   https://your-project-name.vercel.app/
   ```
   Use the password you set in ADMIN_PASSWORD

2. **Admin Panel**
   ```
   https://your-project-name.vercel.app/admin
   ```

3. **API Endpoint (test with a UID)**
   ```
   https://your-project-name.vercel.app/like?uid=123456789&server_name=IND&key=gst
   ```

---

## 🎯 Using Your API

### API Endpoint Format
```
GET /like?uid={USER_ID}&server_name={SERVER}&key=gst
```

### Parameters:
- **uid**: Free Fire user ID (required)
- **server_name**: Server region - `IND`, `BR`, `US`, `SAC`, `NA`, or `BD` (required)
- **key**: Must be `gst` (required for authentication)
- **like**: Optional - number of likes to send or `max` for all tokens

### Examples:

**Send likes to IND server:**
```
https://your-project-name.vercel.app/like?uid=1366626557&server_name=IND&key=gst
```

**Send maximum likes:**
```
https://your-project-name.vercel.app/like?uid=1366626557&server_name=IND&key=gst&like=max
```

**Send specific number of likes:**
```
https://your-project-name.vercel.app/like?uid=1366626557&server_name=IND&key=gst&like=50
```

### Response Format:
```json
{
  "LikesGivenByAPI": 100,
  "LikesAfterCommand": 500,
  "LikesBeforeCommand": 400,
  "PlayerNickname": "GHOST_2XVTDZ",
  "UID": 1366626557,
  "status": 1,
  "TotalTokensAvailable": 5497,
  "TokensUsed": 100,
  "SuccessfulRequests": 98,
  "FailedRequests": 2,
  "SuccessRate": "98.0%"
}
```

---

## 🔧 Common Issues & Solutions

### Issue: "Application Error" 
**Solution**: Make sure both `SECRET_KEY` and `ADMIN_PASSWORD` environment variables are set, then redeploy.

### Issue: "Internal Server Error"
**Solution**: 
1. Go to your deployment in Vercel
2. Click on the deployment
3. Click **"Functions"** tab
4. Check the logs to see the exact error
5. Most common cause: environment variables not set

### Issue: Login not working
**Solution**: 
1. Verify `ADMIN_PASSWORD` is set in environment variables
2. Make sure you redeployed after adding variables
3. Try the exact password you set (case-sensitive)

### Issue: Token errors
**Solution**: Your token file has 5,497 tokens for IND server. If they're expired, you'll need to update the `vercel/api/token_ind.json` file with fresh tokens.

---

## 📊 Token Files

Your current token setup:
- **IND Server**: 5,497 tokens (Real tokens loaded)
- **BR/US/SAC/NA Server**: 2 placeholder tokens (Update if needed)
- **BD Server**: 2 placeholder tokens (Update if needed)

To update tokens for other servers, edit these files:
- `vercel/api/token_br.json` - For Brazil, US, SAC, NA servers
- `vercel/api/token_bd.json` - For Bangladesh server

Format:
```json
[
    {
        "token": "your_jwt_token_here"
    },
    {
        "token": "another_token"
    }
]
```

---

## 🔄 Updating Your Deployment

When you make changes to your code:

1. **Commit and push changes:**
   ```bash
   git add .
   git commit -m "Your update message"
   git push
   ```

2. **Vercel auto-deploys** - Vercel automatically detects the push and redeploys

**OR manually redeploy:**
1. Go to Vercel Dashboard
2. Click **"Deployments"**
3. Click **"⋮"** → **"Redeploy"**

---

## 🌐 Custom Domain (Optional)

To use your own domain:

1. Go to Vercel Dashboard → Your Project
2. Click **"Settings"** → **"Domains"**
3. Enter your domain name
4. Follow the DNS configuration instructions
5. Wait for DNS propagation (up to 48 hours)

---

## 📱 Integration Examples

### cURL
```bash
curl "https://your-project-name.vercel.app/like?uid=1366626557&server_name=IND&key=gst"
```

### JavaScript/Fetch
```javascript
const response = await fetch('https://your-project-name.vercel.app/like?uid=1366626557&server_name=IND&key=gst');
const data = await response.json();
console.log(data);
```

### Python
```python
import requests

url = "https://your-project-name.vercel.app/like"
params = {
    "uid": "1366626557",
    "server_name": "IND",
    "key": "gst"
}

response = requests.get(url, params=params)
print(response.json())
```

---

## 📈 Monitoring & Limits

**Vercel Free Tier Limits:**
- 100 GB bandwidth per month
- Serverless function execution: 100 GB-hours
- Function timeout: 10 seconds max
- 100 deployments per day

**To monitor usage:**
1. Go to Vercel Dashboard
2. Select your project
3. Click **"Analytics"** to see traffic
4. Click **"Deployments"** → Select deployment → **"Functions"** to see logs

---

## 🆘 Support & Troubleshooting

If you encounter issues:

1. **Check Vercel Logs**
   - Go to deployment → Click **"Functions"** tab
   - Look for error messages in red

2. **Verify all files are uploaded**
   - Check that all token JSON files are in `vercel/api/` folder
   - Verify `vercel.json` is in the `vercel/` folder

3. **Test locally (optional)**
   ```bash
   cd vercel/api
   python app.py
   ```
   Then visit `http://localhost:5000`

---

## ✅ Deployment Checklist

Before going live, verify:

- [ ] All code pushed to Git repository
- [ ] Vercel project created with `vercel` as root directory
- [ ] `SECRET_KEY` environment variable set
- [ ] `ADMIN_PASSWORD` environment variable set
- [ ] Project redeployed after adding environment variables
- [ ] All token files present in `vercel/api/` folder
- [ ] Homepage loads and login works
- [ ] API endpoint responds to test requests
- [ ] Admin panel accessible and functional

---

## 🎉 You're All Set!

Your MaxLikes API is now deployed and ready to use. Share your Vercel URL with users or integrate it into your applications!

**Your deployment URL:** `https://your-project-name.vercel.app`

---

*For any deployment issues, check the Vercel function logs or refer to [Vercel's official documentation](https://vercel.com/docs).*
