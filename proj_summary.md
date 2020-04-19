## CITES database

#### 1. introduction

The conservation of biodiversity is a complex problem strongly tight to political actions. The international wildlife trade that includes hundreds of millions of plant and animal specimens is now estimated to be worth billions of dollars annually. The trade is diverse, covering from live animals and plants to a vast array of wildlife products derived from them. However, high level of exploitation of some animal and plant species as well as the trade in them are capable of heavily depleting ther populations and even bring some species to extinction. Many wildlife species in trade are not endangered, but the existence of an agreement to ensure the sustainability of the trade is important in order to safeguard these resources for the future. [1]

Convention on International Trade in Endangered Species of Wild Fauna and Flora, also know as CITES, is an international agreement between governments. Its aim is to ensure that international trade in specimens of wild animals and plants does not threaten their survival. CITES is one of the eight main international agreements relevant to biodiversity (CBD, n.d.) and constitutes a key tool for conservationists, scientists and policy makers.

Currently, the CITES database is open for queries through an R package that provides users with APIs to perform data analytics in R.[2] The source data is also available in the form of CSV files. [3] While it is suitable for small amount of queries and data size, as there are currently more than 2 million records in the database, we consider it can be better organized in the form of a relational database. 

Our project aims at proposing a MySQL database for the CITES organization with all the trading records properly stored for fast retrieveing, as well as the data essential for daily administrative operations. We will also demonstrate the queries with our database and perform sample analysis on the data on our project website.



* [1] https://www.cites.org/eng/disc/what.php
* [2] https://api.speciesplus.net/documentation/v1.html
* [3] https://trade.cites.org/