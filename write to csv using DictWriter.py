from csv import DictWriter
with open('finai.csv') as f:
    csv_writer = DictWriter(f,fieldnames = ['firstname','lastname','age'])
    csv_writer.writeheader()
    # writerow, writerows
    # csv_writer.writerow({
    #     'firstname' : 'harshit'
    #     'lastname' : 'vashistha'
    #     'age' : 500
    # })

    # csv_writer.writerow({
    #     'firstname' : 'harshit'
    #     'lastname' : 'vashistha'
    #     'age' : 500
    # })

    # writerows ----> [dict,dict,dict]
    # csv_writer.writerrows([
    #     {'name' : 'harshit','lastname': 'vashistha','age' :500}
    #     {'name' : 'harshit','lastname': 'vashistha','age' :500}
    #     {'name' : 'harshit','lastname': 'vashistha','age' :500}
    # ])

    