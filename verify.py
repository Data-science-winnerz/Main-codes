import veryfi
import pprint
client_id = "vrfsBsuTmoA7sRrYnF70896ltpih9zr577ZdyS3"
client_secret = "SGMUpyhcUK7wDzUEJlB1cEZUsR3P8Tomap1RCF7m2JYRNKM0Glu7IM1May2DRckEe4v47LvZFUtup6O6I2BV0ubJNXsNFFxint4bOzgxD8pKX61sIpRO3BYdmagDhJdK"
username = "meghanab25"
apikey ="cda358ba87d9306ea887168229c2eb16"
client = veryfi.Client(client_id,client_secret,username,apikey)
categories = ["Travel","Airfare","Lodging","Job Supplies and Materials","Groceres"]
jason_result=client.process_document("C:/Users/MOHAN/Desktop/table extraction/extract-invoice-data-master/jainchem.pdf",categories)
pprint.pprint(jason_result)
