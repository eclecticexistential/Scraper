import csv

def insert_save(email, title, project, experience, company):
	return """
	{0}
	{1}
	Greetings, 
	My programming expertise should be of interest to you. Throughout various {2} projects, I have gained considerable experience in {3}. I would like to discuss who we can utilize these skills to help {4} reach their goals and I hope to be invited to an interview.
	Sincerely,
	Jessica
	""".format(email, title, project, experience, company)

email_to_return = insert_save('beacoder@theinside.com', 'Intern', 'React', 'full stack development', 'The Inside')
	
csv_file = open('unique_email.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow([email_to_return])