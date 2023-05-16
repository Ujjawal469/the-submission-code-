import csv
import requests
from bs4 import BeautifulSoup
url = "https://krittikaiitb.github.io/team/"
source = requests.get(url)   
content1 = source.content
soup = BeautifulSoup(content1, "html.parser")
team_member_sections = soup.find_all("div", class_="tab-content")

# Initialize a list to store the extracted data
team_data = []

# Iterate over each team member section
for tab_content in team_member_sections:
    # Extract the year
    year = tab_content.find("p").text.strip()
    year2=year[5::]

    # Find all team member cards in the section
    member_card = tab_content.find_all("div", class_="container")
    for x in member_card:
        # Iterate over each member card and extract the details
        mmr2=x.find_all("div", class_="col-md-4 mb-4")
        for tju in mmr2:
            name = tju.find("h5").text.strip()
            designation = tju.find("p").text.strip()
            
            # Append the data to the team_data list
            team_data.append([name, designation, year2])   
                # Extract the name and designation

# Save the extracted data to a CSV file
csv_filename = "krittika_team_data.csv"
with open(csv_filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "Designation", "Year"])  # Write the header
    writer.writerows(team_data)  # Write the data rows

print(f"Data successfully scraped and saved to {csv_filename}.")