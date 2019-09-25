# Import packages
import matplotlib.pyplot as plt
import seaborn as sns
from pytrends.request import TrendReq

# Define Google Trends API
pytrend = TrendReq()

kw_list = ["malaria symptoms"]
# related_queries_dict = pytrend.related_queries()
# print(related_queries_dict)

pytrend.build_payload(kw_list, geo='IN')

# Over time-in India
malaria_df = pytrend.interest_over_time()
print(malaria_df.head())

# Plot
sns.set(rc={'figure.figsize':(11, 4)})

list(malaria_df.columns)
malaria_df.index.name = 'date'
malaria_df.reset_index(inplace=True)
list(malaria_df.columns)
malaria_df.columns = ['date', 'malaria', 'isPartial']
list(malaria_df.columns)

ax = plt.gca()
plt.plot(malaria_df.malaria, linewidth=0.5, color="red")
ax.set_ylabel('Relative Search Volume')
ax.set_title('Google Trends for "malaria symptoms" in India', fontsize=14)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.MonthFormatter('%b %d'))
plt.savefig("malaria.png")




