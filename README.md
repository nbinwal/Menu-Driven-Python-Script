# Menu-Driven-Python-Script
Menu Driven Python Script for Azure Advisor Data Visualization 
### **📜 Explanation of Each Menu Option in the Script**

This **menu-driven Python script** allows users to generate various **pie and bar charts** based on **Azure Advisor recommendations data** from a CSV file.  

It supports **High, Medium, and Low Business Impact** insights, as well as **cost savings analysis**.  

#### **💡 How It Works**
1. The script **reads the CSV file** (Azure Advisor recommendations).  
2. It **cleans and processes the data** (handling text and numeric values).  
3. The **menu appears**, allowing the user to **choose which chart to generate**.  
4. The script **filters the data** based on the selection.  
5. It then **generates the requested chart** using **Matplotlib**.

---

### **🔹 Menu Options Breakdown**
Each menu option corresponds to **a specific type of chart** and data analysis.

| **Menu Option** | **Description** | **Chart Type** |
|---------------|----------------|--------------|
| **1. High Impact Recommendations by Category** | Groups **High Business Impact** recommendations by **Category** (e.g., Cost, Security, Performance, etc.). | 📊 **Pie Chart** |
| **2. High Impact Recommendations by Recommendation** | Shows which **specific recommendations** have the most **High Impact**. | 📊 **Pie Chart** |
| **3. High Impact Recommendations by Azure Resource Type** | Displays which **Azure Resource Types** (VMs, Storage, Databases, etc.) have the most **High Impact** recommendations. | 📊 **Pie Chart** |
| **4. High & Medium Impact Recommendations by Category** | Groups **High & Medium Business Impact** recommendations by **Category**. | 📊 **Pie Chart** |
| **5. Business Impact: High vs Medium vs Low** | Compares the overall number of **High, Medium, and Low Impact** recommendations. | 📊 **Pie Chart** |
| **6. High & Medium Impact Recommendations by Subscription Name** | Groups **High & Medium Impact** recommendations by **Subscription Name**. | 📊 **Pie Chart** |
| **7. Cost Recommendations by Potential Annual Cost Savings** | Analyzes **cost-related recommendations** based on **potential cost savings**. | 📊 **Pie Chart** |
| **8. Cost Savings by Resource Group & Type (Pie Chart)** | Displays **cost savings** grouped by **Resource Group** and **Azure Resource Type**. | 📊 **Pie Chart** |
| **9. Cost Savings by Resource Group & Type (Bar Chart)** | Similar to option 8, but **shows cost savings in a bar chart** format. | 📊 **Bar Chart** |
| **q. Quit** | Exits the script. | ❌ |

---

### **🔹 Explanation of Each Option in Detail**
Let's break down **what happens behind the scenes** when you choose a menu option.

---

### **📌 1. High Impact Recommendations by Category**
🔹 **What it does:**  
- **Filters for High Business Impact recommendations.**  
- **Groups them by Category.**  
- **Creates a Pie Chart** showing which **categories** (Cost, Security, Performance, etc.) have the most recommendations.

📊 **Chart Example:**  
- **50%** Cost  
- **30%** Security  
- **20%** Performance  

**👉 Purpose:** Helps understand **which recommendation category needs immediate attention**.

---

### **📌 2. High Impact Recommendations by Recommendation**
🔹 **What it does:**  
- **Filters for High Business Impact recommendations.**  
- **Groups them by specific recommendation name.**  
- **Creates a Pie Chart** showing the most frequent **recommendations**.

📊 **Chart Example:**  
- **40%** "Resize VM for cost optimization"  
- **30%** "Enable Azure Security Center"  
- **20%** "Enable Backup for VMs"  
- **10%** Others  

**👉 Purpose:** Helps identify the **most common high-impact recommendations** across subscriptions.

---

### **📌 3. High Impact Recommendations by Azure Resource Type**
🔹 **What it does:**  
- **Filters for High Business Impact recommendations.**  
- **Groups them by Azure Resource Type (VMs, Storage, Databases, etc.).**  
- **Creates a Pie Chart** showing which resource types have the most recommendations.

📊 **Chart Example:**  
- **45%** Virtual Machines  
- **30%** SQL Databases  
- **15%** Storage Accounts  
- **10%** Others  

**👉 Purpose:** Helps identify which **Azure resources need immediate optimization**.

---

### **📌 4. High & Medium Impact Recommendations by Category**
🔹 **What it does:**  
- **Filters for both High & Medium Business Impact recommendations.**  
- **Groups them by Category.**  
- **Creates a Pie Chart** comparing different categories.

📊 **Chart Example:**  
- **60%** Cost  
- **25%** Security  
- **15%** Performance  

**👉 Purpose:** Helps prioritize **not just high but also medium-impact recommendations**.

---

### **📌 5. Business Impact: High vs Medium vs Low**
🔹 **What it does:**  
- **Counts all recommendations** based on Business Impact.  
- **Creates a Pie Chart** comparing High, Medium, and Low impact recommendations.

📊 **Chart Example:**  
- **50%** High  
- **30%** Medium  
- **20%** Low  

**👉 Purpose:** Helps measure **how critical the recommendations are overall**.

---

### **📌 6. High & Medium Impact Recommendations by Subscription Name**
🔹 **What it does:**  
- **Filters for High & Medium Impact recommendations.**  
- **Groups them by Subscription Name.**  
- **Creates a Pie Chart** showing which **Azure Subscriptions** have the most recommendations.

📊 **Chart Example:**  
- **50%** "Production Subscription"  
- **30%** "Dev/Test Subscription"  
- **20%** "Staging Subscription"  

**👉 Purpose:** Helps determine which **subscription needs the most attention**.

---

### **📌 7. Cost Recommendations by Potential Annual Cost Savings**
🔹 **What it does:**  
- **Filters for "Cost" recommendations.**  
- **Groups them by Recommendation.**  
- **Sums up Potential Annual Cost Savings** to show the highest cost-saving actions.  
- **Creates a Pie Chart**.

📊 **Chart Example:**  
- **$20,000** - "Resize VM to a lower SKU"  
- **$15,000** - "Enable Reserved Instances"  
- **$10,000** - "Remove Unused Resources"  

**👉 Purpose:** Helps **identify the biggest cost-saving opportunities**.

---

### **📌 8. Cost Savings by Resource Group & Type (Pie Chart)**
🔹 **What it does:**  
- **Filters for "Cost" recommendations.**  
- **Groups cost savings by Resource Group & Azure Resource Type.**  
- **Creates a Pie Chart** showing cost savings distribution.

📊 **Chart Example:**  
- **$30,000** - Resource Group "WebApp-RG" (VMs)  
- **$25,000** - Resource Group "SQL-DB-RG" (Databases)  
- **$15,000** - Resource Group "Storage-RG" (Blob Storage)  

**👉 Purpose:** Helps pinpoint **which resource group will save the most money**.

---

### **📌 9. Cost Savings by Resource Group & Type (Bar Chart)**
🔹 **What it does:**  
- **Filters for "Cost" recommendations.**  
- **Groups cost savings by Resource Group & Type.**  
- **Creates a Bar Chart**.

📊 **Chart Example:**  
A **bar chart** with **cost savings values displayed on top**.

| Resource Group | Cost Savings ($) |
|---------------|-----------------|
| WebApp-RG | **$30,000** |
| SQL-DB-RG | **$25,000** |
| Storage-RG | **$15,000** |

**👉 Purpose:** Provides a **detailed financial impact analysis**.

---

### **📌 q. Quit**
🔹 **What it does:**  
- **Exits the program.**  
- **No charts are generated.**

---

### **🎯 Final Thoughts**
🚀 This script **helps clients prioritize Azure recommendations efficiently**.  
It provides **visual clarity** on **business impact, cost savings, and resource optimizations**.
