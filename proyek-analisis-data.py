import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
data = pd.read_csv("all_merged_df.csv")  # Gantilah "nama_file.csv" dengan nama file yang sesuai

# Sidebar
st.sidebar.title("Dashboard Options")
selected_option = st.sidebar.selectbox("Select Dashboard Option", ["Overview", "Product Analysis", "Order Analysis", "Customer Analysis"])

# Dashboard Options
if selected_option == "Overview":
    # Display overview statistics
    st.title("Overview Dashboard")
    st.write("This section provides an overview of the dataset.")

    # Display summary statistics
    st.write("### Summary Statistics")
    st.write(data.describe())

    # Display order status distribution
    st.write("### Order Status Distribution")
    order_status_counts = data['order_status'].value_counts()
    st.bar_chart(order_status_counts)

elif selected_option == "Product Analysis":
    # Display product-related analysis
    st.title("Product Analysis Dashboard")
    st.write("This section provides analysis related to products.")

    # Display product categories
    st.write("### Product Categories")
    product_category_counts = data['product_category_name_english'].value_counts()
    st.bar_chart(product_category_counts)

    # Display product ratings
    st.write("### Product Ratings")
    fig = px.histogram(data, x='review_score', title='Distribution of Product Ratings')
    st.plotly_chart(fig)

elif selected_option == "Order Analysis":
    # Display order-related analysis
    st.title("Order Analysis Dashboard")
    st.write("This section provides analysis related to orders.")

    # Display order timeline
    st.write("### Order Timeline")
    order_timeline = data[['order_date', 'order_id']].groupby('order_date').count()
    fig = px.line(order_timeline, x=order_timeline.index, y='order_id', title='Order Timeline')
    st.plotly_chart(fig)

    # Display payment method distribution
    st.write("### Payment Method Distribution")
    payment_method_counts = data['payment_type'].value_counts()
    fig = px.pie(
        names=list(payment_method_counts.index),
        values=list(payment_method_counts.values),
        title='Distribution of Payment Methods'
    )
    st.plotly_chart(fig)

elif selected_option == "Customer Analysis":
    # Display customer-related analysis
    st.title("Customer Analysis Dashboard")
    st.write("This section provides analysis related to customers.")

    # Display customer locations
    st.write("### Customer Locations")
    customer_locations = data[['customer_city', 'customer_state']].groupby(['customer_city', 'customer_state']).size().reset_index(name='counts')
    fig = px.scatter_geo(customer_locations, locationmode='USA-states', locations='customer_state', color='counts',
                         hover_name='customer_city', title='Customer Locations')
    st.plotly_chart(fig)

    # Display customer satisfaction
    st.write("### Customer Satisfaction")
    avg_review_score = data['review_score'].mean()
    st.write(f"The average customer review score is: {avg_review_score:.2f}")

elif selected_option == "Order Analysis":
    # Display order-related analysis
    st.title("Order Analysis Dashboard")
    st.write("This section provides analysis related to orders.")

    # Display order timeline
    st.write("### Order Timeline")
    order_timeline = data[['order_date', 'order_id']].groupby('order_date').count()
    fig = px.line(order_timeline, x=order_timeline.index, y='order_id', title='Order Timeline')
    st.plotly_chart(fig)

    # Display payment method distribution
    st.write("### Payment Method Distribution")
    payment_method_counts = data['payment_type'].value_counts()
    fig1 = px.pie(
        names=list(payment_method_counts.index),
        values=list(payment_method_counts.values),
        title='Distribution of Payment Methods'
    )
    st.plotly_chart(fig1)

    # Display freight value distribution
    st.write("### Distribution of Freight Value")
    fig2 = px.histogram(data, x='freight_value', title='Distribution of Freight Value')
    st.plotly_chart(fig2)

    # Display average order value over time
    st.write("### Average Order Value Over Time")
    avg_order_value_over_time = data.groupby('order_date')['payment_value'].mean().reset_index()
    fig3 = px.line(avg_order_value_over_time, x='order_date', y='payment_value', title='Average Order Value Over Time')
    st.plotly_chart(fig3)


# Additional analysis options can be added based on your specific requirements
