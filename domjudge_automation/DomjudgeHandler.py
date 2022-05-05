import WebController
import csv

DOMJUDGE_USERNAME = ''
DOMJUDGE_PASSWORD = ''

FORM_CSV_PATH = ''
ACCOUNTS_CSV_FILE_NAME = ''
TEAMNAME_ROW_NAME = ''
FIRST_TEAM_ID = 1
LAST_TEAM_ID = 150  # change this value


class DomjudgeHandler:
    def __init__(self, username, password):
        self.controller = WebController.DomjudgeController()
        self.controller.signin(username, password)

    def create_team_member_and_save_as_csv(self, save_as, name_prefix, start_team_id, end_team_id):
        def create_name_based_on_index(prefix, index):
            name = prefix + '%d' % index if index > 99 else '0%d' % index if index > 9 else '00%d' % index
            return name

        with open(save_as, 'a', newline='') as account_file:
            csv_writer = csv.writer(account_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(start_team_id, end_team_id + 1):
                user_name = create_name_based_on_index(name_prefix, i)
                user_account_info = self.controller.create_team_member(team_id=i, user_name=user_name)
                csv_writer.writerow([user_account_info['username'], user_account_info['password']])

    def set_all_team_name(self, csv_path, start_team_id):
        with open(csv_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            team_id = start_team_id
            for row in reader:
                team_display_name = row[TEAMNAME_ROW_NAME]
                self.controller.set_team_name(team_id, team_display_name)
                team_id += 1


if __name__ == "__main__":
    handler = DomjudgeHandler(DOMJUDGE_USERNAME, DOMJUDGE_PASSWORD)
    # handler.create_team_member_and_save_as_csv(ACCOUNTS_CSV_FILE_NAME, 'user', FIRST_TEAM_ID, LAST_TEAM_ID)
    # handler.set_all_team_name(FORM_CSV_PATH, FIRST_TEAM_ID)
