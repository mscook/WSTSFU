from csvkit.utilities.in2csv import In2CSV


def build_csv_from_excel():

    args = ['/home/mscook/Desktop/Projects/ST131_99/TableS1.xlsx']
    output_file = open('acme.csv', mode='w+', buffering=-1)
    utility = In2CSV(args, output_file)
    utility.main()
