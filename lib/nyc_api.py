import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"
        response = requests.get(URL)
        return response.content

    def program_school(self):
        # Parse the API response and extract the list of programs
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

# Create an instance of GetPrograms
get_programs_instance = GetPrograms()

# Call the program_school method to obtain the list of programs
program_school_list = get_programs_instance.program_school()

# Iterate over the list of schools
for school in set(program_school_list):
    print(school)
