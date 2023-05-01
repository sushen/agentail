import gspread


class Connection:
    @staticmethod
    def connect_worksheet(worksheet_name="fb_profile"):
        gc = gspread.service_account(r'../studentfindergspreed-7fdad14f5755.json')
        spreadsheet = gc.open("Employee")
        worksheet = spreadsheet.worksheet(worksheet_name)
        return worksheet


if __name__ == "__main__":
    ws = Connection().connect_worksheet("fb_profile")
    group_list = ws.col_values(1)
    print(group_list)
