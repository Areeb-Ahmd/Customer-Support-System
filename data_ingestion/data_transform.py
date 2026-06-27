import pandas as pd
from langchain_core.documents import Document


class data_converter:

    def __init__(self):
        print('data converter initialized..')
        self.product_data = pd.read_csv(r"D:\Coding\Projects\Customer Support System\data\flipkart_product_review.csv")
        #print(self.product_data.head())

    def data_transformation(self):
        # Select only the required columns
        required_cols = self.product_data.columns
        required_cols = list(required_cols[1:])
        #print(required_cols)

        product_list = []
        # Iterate through the dataframe
        for index, row in self.product_data.iterrows():
            object = {
                "product_name": row['product_title'],
                "product_rating": row['rating'],
                "summary": row['summary'],
                "product_review": row['review']
            }
            product_list.append(object)

        #print('Below is product list:')
        #print(product_list[0])

        docs = []
        for entry in product_list:
            metadata =  {
                "product_name":entry['product_name'], 
                "product_rating":entry['product_rating'], 
                "summary":entry['summary']
            }
            doc = Document(page_content=entry['product_review'], metadata=metadata)
            docs.append(doc)
        #print(docs[0])
        return docs
         
           
if __name__ == '__main__':
    data_convert = data_converter()
    data_convert.data_transformation()
