import pandas as pd
import matplotlib.pyplot as plt
import textwrap
import matplotlib.ticker as mticker
import os

# -----------------------------
# 🔹 Utility Functions
# -----------------------------

def plot_pie_chart(data, group_col, title, top_n=8, wrap_width=30):
    counts = data[group_col].value_counts()
    if len(counts) > top_n:
        top_counts = counts.iloc[:top_n]
        others_sum = counts.iloc[top_n:].sum()
        counts = pd.concat([top_counts, pd.Series({'Others': others_sum})])
    
    labels = ["\n".join(textwrap.wrap(label, width=wrap_width)) for label in counts.index]
    
    plt.figure(figsize=(10, 10))
    plt.pie(counts, labels=labels, autopct="%1.1f%%", startangle=140, wedgeprops={'edgecolor': 'white'})
    plt.title(title, fontsize=14)
    plt.show()

def plot_bar_chart(labels, values, title, xlabel, ylabel, wrap_width=30):
    wrapped_labels = ["\n".join(textwrap.wrap(label, width=wrap_width)) for label in labels]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(wrapped_labels, values, color='skyblue', edgecolor='black')
    
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    ax.set_title(title, fontsize=16)
    
    plt.xticks(rotation=45, ha='right')
    formatter = mticker.FuncFormatter(lambda x, pos: f'${x:,.2f}')
    ax.yaxis.set_major_formatter(formatter)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'${height:,.2f}', 
                    xy=(bar.get_x() + bar.get_width()/2, height),
                    xytext=(0, 5), 
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    plt.show()

# -----------------------------
# 🔹 Data Loading & Filtering
# -----------------------------

csv_path = "/Users/mohanchandrabinwal/Downloads/Advisor_2025-02-01T14_38_16.311Z.csv"

if not os.path.exists(csv_path):
    print(f"Error: File not found at {csv_path}")
    exit()

df = pd.read_csv(csv_path, encoding="utf-8")
df.columns = df.columns.str.strip()

def filter_by_impact(df, impacts):
    impacts = [imp.lower() for imp in impacts]
    return df[df["Business Impact"].str.strip().str.lower().isin(impacts)].copy()

# -----------------------------
# 🔹 Menu System
# -----------------------------

def show_menu():
    print("\nSelect the chart you want to generate:")
    print("1. High Impact Recommendations by Category")
    print("2. High Impact Recommendations by Recommendation")
    print("3. High Impact Recommendations by Azure Resource Type")
    print("4. High & Medium Impact Recommendations by Category")
    print("5. Business Impact: High vs Medium vs Low")
    print("6. High & Medium Impact Recommendations by Subscription Name")
    print("7. Cost Recommendations by Potential Annual Cost Savings")
    print("8. Cost Savings by Resource Group & Type (Pie Chart)")
    print("9. Cost Savings by Resource Group & Type (Bar Chart)")
    print("q. Quit")

def menu_choice():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip().lower()
        if choice == 'q':
            print("Exiting...")
            break
        
        # (1): High Impact by Category
        if choice == '1':
            high_df = filter_by_impact(df, ["high"])
            plot_pie_chart(high_df, "Category", "High Impact Recommendations by Category")
        
        # (2): High Impact by Recommendation
        elif choice == '2':
            high_df = filter_by_impact(df, ["high"])
            plot_pie_chart(high_df, "Recommendation", "High Impact Recommendations by Recommendation")
        
        # (3): High Impact by Type (Azure Resource Type)
        elif choice == '3':
            high_df = filter_by_impact(df, ["high"])
            plot_pie_chart(high_df, "Type", "High Impact Recommendations by Type")
        
        # (4): High & Medium Impact by Category
        elif choice == '4':
            hm_df = filter_by_impact(df, ["high", "medium"])
            plot_pie_chart(hm_df, "Category", "Recommendations by Category (High & Medium Impact)")
        
        # (5): Business Impact: High vs Medium vs Low
        elif choice == '5':
            impact_df = filter_by_impact(df, ["high", "medium", "low"])
            impact_counts = impact_df["Business Impact"].str.strip().str.lower().value_counts()
            impact_counts.index = impact_counts.index.str.capitalize()
            plt.figure(figsize=(8, 8))
            plt.pie(impact_counts, labels=impact_counts.index, autopct="%1.1f%%", startangle=140, wedgeprops={'edgecolor': 'black'})
            plt.title("Business Impact: High vs Medium vs Low")
            plt.show()
        
        # (6): High & Medium Impact by Subscription Name
        elif choice == '6':
            hm_df = filter_by_impact(df, ["high", "medium"])
            plot_pie_chart(hm_df, "Subscription Name", "Recommendations by Subscription Name (High & Medium Impact)")

        # (7): Cost Recommendations by Potential Annual Cost Savings
        elif choice == '7':
            cost_df = filter_by_impact(df, ["high"])
            plot_pie_chart(cost_df, "Recommendation", "Cost Recommendations by Potential Annual Cost Savings")

        # (8): Cost Savings by Resource Group & Type (Pie Chart)
        elif choice == '8':
            cost_df = filter_by_impact(df, ["high"])
            plot_pie_chart(cost_df, "Resource Group", "Cost Savings by Resource Group & Type")

        # (9): Cost Savings by Resource Group & Type (Bar Chart) - **Fixed Version**
        elif choice == '9':
            cost_df = filter_by_impact(df, ["high"])

            # ✅ FIX: Convert "Potential Annual Cost Savings" to numeric
            cost_df["Potential Annual Cost Savings Cleaned"] = pd.to_numeric(
                cost_df["Potential Annual Cost Savings"].astype(str).str.replace(r'[^\d.]', '', regex=True),
                errors="coerce"
            )

            # ✅ Use cleaned column to group and sort values
            grouped = cost_df.groupby("Resource Group")["Potential Annual Cost Savings Cleaned"].sum().sort_values(ascending=False)

            if not grouped.empty:
                plot_bar_chart(grouped.index.tolist(), grouped.values, "Cost Savings by Resource Group & Type", "Resource Group", "Total Cost Savings (USD)")
            else:
                print("No valid cost savings data available.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu_choice()
