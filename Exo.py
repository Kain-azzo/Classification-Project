import prepare
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu


def security_impact(isp):
    '''Determines if gender has any impact on security bundle purchase, accepts gender and security backup as inputs, accepts       dataframe'''
    Male = isp[isp.gender == 0]
    Female = isp[isp.gender == 1]

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Plotting the first bar graph for "Male"
    axs[0].bar(['Security Backup', 'No Security Backup'], Male.security_backup.value_counts(), color=['hotpink', 'skyblue'], alpha=0.7)
    axs[0].set_title("Male")
    axs[0].set_ylabel("Count")

    # Plotting the second bar graph for "Female"
    axs[1].bar(['Security Backup', 'No Security Backup'], Female.security_backup.value_counts(), color=['hotpink', 'skyblue'], alpha=0.7)
    axs[1].set_title("Female")
    axs[1].set_ylabel("Count")

    plt.suptitle("Security Backup Comparison by Gender")

    plt.show()

def gender_impact(isp):
    '''Determines if gender has any impact on churn rates, accepts gender and churn as inputs, accepts dataframe'''
    Male = isp[isp.gender == 0]
    Female = isp[isp.gender == 1]
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Plotting the first bar graph for "Male"
    axs[0].bar(['Churned', 'Not Churned'], Male.churn.value_counts(), color='blue', alpha=0.7)
    axs[0].set_title("Male")
    axs[0].set_ylabel("Count")

    # Plotting the second bar graph for "Female"
    axs[1].bar(['Churned', 'Not Churned'], Female.churn.value_counts(), color='orange', alpha=0.7)
    axs[1].set_title("Female")
    axs[1].set_ylabel("Count")

    # Adding a common title for the entire subplot
    plt.suptitle("Churn Comparison by Gender")

    # Display the plot
    plt.show()
    
def senior_citizen_churn(isp):
    '''Determines if senior citizens churn faster than non seniors, senior citizens and churn as inputs, accepts dataframe'''
    senior_citizen_data = isp[isp['senior_citizen']==1]

    # Calculate the churn rate for senior citizens
    senior_citizen_churn_rate = senior_citizen_data['churn'].mean()

    # Calculate the churn rate for non-senior citizens
    non_senior_citizen_data = isp[isp['senior_citizen']==0]
    non_senior_citizen_churn_rate = non_senior_citizen_data['churn'].mean()

    # Create a pie chart
    labels = ['Senior Citizen', 'Not Senior Citizen']
    sizes = [senior_citizen_churn_rate, non_senior_citizen_churn_rate]
    colors = ['gold', 'green']

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))

    plt.title('Churn Rate Comparison by Senior Citizenship')
    plt.show()
    
    
    
def churners(isp):
    '''Determines if customers churn faster as monthly rates increase, monthly charges and churn as inputs, accepts   
    dataframe'''
    did_churn = isp[isp.churn == 1]
    didnt_churn= isp[isp.churn == 0]

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Plotting the first histogram for "did churn"
    axs[0].hist(did_churn.monthly_charges, label="did churn", color='blue')
    axs[0].set_title("Did Churn")
    axs[0].legend()

    # Plotting the second histogram for "didn't churn"
    axs[1].hist(didnt_churn.monthly_charges, label="didn't churn", color='orange')
    axs[1].set_title("Didn't Churn")
    axs[1].legend()

    # Adding a common title for the entire subplot
    plt.suptitle("Monthly Charges Comparison")

    # Display the plot
    plt.show()
    

def churner_mannwit(isp):
    '''Prints out results of mannwhitney test with senior citizens and churn as inputs, accepts dataframe'''
    charges_churned = isp.loc[isp['churn'] == 1, 'monthly_charges']
    charges_non_churned = isp.loc[isp['churn'] == 0, 'monthly_charges']

    # Perform Mann-Whitney U test
    result = mannwhitneyu(charges_churned, charges_non_churned)

    # Display the result
    print(f'Mann-Whitney U Statistic: {result.statistic}')
    print(f'P-value: {result.pvalue}')

    # Interpret the result
    alpha = 0.05
    if result.pvalue < alpha:
        print("Reject the null hypothesis. There is a significant difference in monthly charges between churned and non-churned         customers.")
    else:
        print("Fail to reject the null hypothesis. There is no significant difference in monthly charges between churned and           non-churned customers.")
        
def senior_mannwit(isp):
    '''Prints out results of mannwhitney test with churn and monthiy charges as inputs, accepts dataframe'''
    charges_senior_churned = isp.loc[(isp['churn'] == 1) & (isp['senior_citizen'] == 0),'monthly_charges']
    charges_senior_non_churned = isp.loc[(isp['churn'] == 0) & (isp['senior_citizen'] == 0),'monthly_charges']

    # Check if samples are non-empty before performing Mann-Whitney U test
    if len(charges_senior_churned) > 0 and len(charges_senior_non_churned) > 0:
        # Perform Mann-Whitney U test
        result_senior = mannwhitneyu(charges_senior_churned, charges_senior_non_churned)

        # Display the result
        print(f'Mann-Whitney U Statistic (Senior Citizens): {result_senior.statistic}')
        print(f'P-value: {result_senior.pvalue}')

        # Interpret the result
        alpha = 0.05
        if result_senior.pvalue < alpha:
            print("Reject the null hypothesis. There is a significant difference in monthly charges between churned and  non-               churned senior citizens.")
        else:
            print("Fail to reject the null hypothesis. There is no significant difference in monthly charges between churned               and non-churned senior citizens.")

