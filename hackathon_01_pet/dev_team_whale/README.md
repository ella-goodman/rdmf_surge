# Hi Team Whale :whale2:

This is your space for development work. Feel free to use this folder for saving and sharing files that are experimental, in-progress, tests, etc.

	• Customer requests data
	• JIRA ticket to action the request
	• User actioning the request works in a spark environment in GCP
		○ Global variable for project_id 
		○ Make a call to a table with the api_key, and get back the project_id
		○ Dataproc
		○ Cloud run - trigger scripts
		○ Cloud functions
		○ Create an API that calls the tables
		○ Preference for doing the encryption within the spark environment/code that is running in the spark environment
		○ Sort the rows randomly
	• Where we actually store the data
		○ Bigquery
		○ Store the data tables in bigquery
		○ Store our (customer_name, project_id) lookup in table in bigquery
			§ Can we just expose the project_id?
			§ If not, keep a table customer_name, project_id
			§ Does GCP have another option for storing a protected lookup?
			§ Does it make a difference if customer_a has projects x,y,z. 
			§ Need a function for adding a new row to this table
		○ Table for keeping track of columns that have been shared with a project_id
		○ Want an API that gets tables from BigQuery
	• Encryption/transformation algorithm
		○ Adds the project_id as a salt to any master id columns, on all tables we have retrieved (concat the salt to the end of each row id)
		○ Hashes the salted master id columns (both these could be done in the same step)
		○ Apply a random sort to it in some way
		○ Then the data engineer transform/joins the data - gets specific dataset the customer wants
	• How we get data from big query into our scripts being ran in spark environment
Build our own api that gets whole tables back - bigquery have an api for this
