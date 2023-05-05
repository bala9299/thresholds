import streamlit as st
import pandas as pd
import plotly.express as px



def main():
    st.write("Upload the first dataframe (df1)")
    df1_file = st.file_uploader("Choose a CSV file", type='csv')
    if df1_file is not None:
        df1 = pd.read_csv(df1_file)
        st.write(df1)

        cumsum_col = df1['Balance'].cumsum()

        df1['cum_Balance'] = cumsum_col

        df1 = df1.reset_index()

        total_sum = df1['Balance'].sum()
        st.write("the total balance value",total_sum)

        navigate = st.radio("**select % here**",["10%","20%","25%","50%"])

        if navigate == "10%":        
            thresholds = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

            index_diffs = []
            st.write("10% of total balance : ",0.1 * total_sum)

            for i in range(len(thresholds)):
                threshold = thresholds[i] * total_sum
                
                if i == len(thresholds) - 1:
                    index = df1['index'].max()
                else:
                    index = df1[df1['cum_Balance'] >= threshold]['index'].min()

                if i == 0:
                    index_diffs.append(index + 1)
                else:
                    index_diff = index - prev_index
                    index_diffs.append(index_diff)

                prev_index = index

                st.write(f"The threshold for  {int(thresholds[i]*100)}% of the total summed up value is reached at index {index}.")
                st.write(f"The number of indices between the previous threshold and the current threshold is {index_diffs[i]}.")

            fig = px.bar(x=[f'{int(thresholds[i]*100)}%' for i in range(len(thresholds))], y=index_diffs, labels={'x': 'Threshold', 'y': 'Number of Indices'})
            fig.update_layout(title={'text': 'Number of Indices for Different Thresholds', 'x': 0.5})
            fig.update_traces(text=index_diffs, textposition='outside')
            st.plotly_chart(fig)


        if navigate == "20%":
            thresholds = [0.2, 0.4, 0.6, 0.8, 1.0]

            index_diffs = []
            st.write("20% of total balance : ",0.2 * total_sum)

            for i in range(len(thresholds)):
                threshold = thresholds[i] * total_sum
                
                if i == len(thresholds) - 1:
                    index = df1['index'].max()
                else:
                    index = df1[df1['cum_Balance'] >= threshold]['index'].min()

                if i == 0:
                    index_diffs.append(index + 1)
                else:
                    index_diff = index - prev_index
                    index_diffs.append(index_diff)

                prev_index = index

                st.write(f"The threshold for  {int(thresholds[i]*100)}% of the total summed up value is reached at index {index}.")
                st.write(f"The number of indices between the previous threshold and the current threshold is {index_diffs[i]}.")

            fig = px.bar(x=[f'{int(thresholds[i]*100)}%' for i in range(len(thresholds))], y=index_diffs, labels={'x': 'Threshold', 'y': 'Number of Indices'})
            fig.update_layout(title={'text': 'Number of Indices for Different Thresholds', 'x': 0.5})
            fig.update_traces(text=index_diffs, textposition='outside')
            st.plotly_chart(fig)


        if navigate == "25%":
            thresholds = [0.25, 0.5, 0.75, 1.0]
            index_diffs = []
            st.write("25% of total balance : ",0.25 * total_sum)

            for i in range(len(thresholds)):
                threshold = thresholds[i] * total_sum
                
                if i == len(thresholds) - 1:
                    index = df1['index'].max()
                else:
                    index = df1[df1['cum_Balance'] >= threshold]['index'].min()

                if i == 0:
                    index_diffs.append(index + 1)
                else:
                    index_diff = index - prev_index
                    index_diffs.append(index_diff)

                prev_index = index
                st.write(f"The threshold for the {int(thresholds[i]*100)}% of the total summed up value is reached at index {index}.")
                st.write(f"The number of indices between the previous threshold and the current threshold is {index_diffs[i]}.")
            fig = px.bar(x=[f'{int(thresholds[i]*100)}%' for i in range(len(thresholds))], y=index_diffs, labels={'x': 'Threshold', 'y': 'Number of Indices'})
            fig.update_layout(title={'text': 'Number of Indices for Different Thresholds', 'x': 0.5})
            fig.update_traces(text=index_diffs, textposition='outside')
            st.plotly_chart(fig)

        if navigate == "50%":
            thresholds = [0.5,1.0]
            index_diffs = []
            st.write("50% of total balance : ",0.5 * total_sum)

            for i in range(len(thresholds)):
                threshold = thresholds[i] * total_sum
                
                if i == len(thresholds) - 1:
                    index = df1['index'].max()
                else:
                    index = df1[df1['cum_Balance'] >= threshold]['index'].min()

                if i == 0:
                    index_diffs.append(index + 1)
                else:
                    index_diff = index - prev_index
                    index_diffs.append(index_diff)

                prev_index = index
                st.write(f"The threshold for the {int(thresholds[i]*100)}% of the total summed up value is reached at index {index}.")
                st.write(f"The number of indices between the previous threshold and the current threshold is {index_diffs[i]}.")
            fig = px.bar(x=[f'{int(thresholds[i]*100)}%' for i in range(len(thresholds))], y=index_diffs, labels={'x': 'Threshold', 'y': 'Number of Indices'})
            fig.update_layout(title={'text': 'Number of Indices for Different Thresholds', 'x': 0.5})
            fig.update_traces(text=index_diffs, textposition='outside')
            st.plotly_chart(fig)





if __name__ == "__main__":
    main()