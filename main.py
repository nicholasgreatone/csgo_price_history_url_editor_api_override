link_template = "https://steamcommunity.com/market/pricehistory/?country=US&currency=1&appid=730&market_hash_name={casename}"


meow = '{  }'
# Read case names from skins_list.txt
with open("skins_list.txt", "r") as file:
    case_names = file.read().splitlines()

# Create a new file for modified links
with open("modified_links.txt", "w") as modified_file, \
     open("formatted_case_names.txt", "w") as formatted_file:
    for case_name in case_names:
        modified_link = link_template.replace("{casename}", case_name)
        modified_file.write(f' \n {modified_link} \n')

        formatted_case_name = case_name.replace("%20", "_")
        formatted_file.write(f'\n{formatted_case_name}  =  \n')

print("Modified links and formatted case names have been written to files.")


