import streamlit as st
import time
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import app


# Set the page layout to wide
st.set_page_config(layout="wide")

st.title("Automobile Loan Default Prediction System")

# Create tabs for Home and Prediction Form
tab1, tab2 = st.tabs(["Home", "Prediction Form"])

# Home page with image slideshow and additional sections
with tab1:
    # Initialize session state variables
    if "images" not in st.session_state:
        st.session_state.images = [
            "static/Car1.png",
            "static/Car3.jpg",
            "static/car2.png",
        ]
        st.session_state.descriptions = [
            " ",
            " ",
            " ",
        ]
        st.session_state.current_index = 0

    # Display the current image with caption
    st.image(
        st.session_state.images[st.session_state.current_index],
        use_column_width=True,
        caption=st.session_state.descriptions[st.session_state.current_index],
    )

    # Move to the next image automatically after a delay (e.g., 3 seconds)
    time.sleep(3)

    # Update the current image index
    st.session_state.current_index = (st.session_state.current_index + 1) % len(st.session_state.images)

    # Title and description for the Home page
    st.header("Welcome to Automobile Loan Default Prediction System")
    st.write("""<p style="text-align: justify;">
        Non-Banking Financial Institutions (NBFIs) are financial entities 
        without a full banking license and are not governed by the same regulations as traditional banks. 
        They enhance economic accessibility by offering vital services such as investment consultancy, risk pooling, 
        and marketing brokering. NBFIs can cater to clients with more flexible credit requirements compared to conventional banks.
    </p>""", unsafe_allow_html=True)

    st.markdown(
        """
        <hr style="border: 3px solid #FFDF00; width: 100%; margin: auto; border-radius: 50px">
        """,
        unsafe_allow_html=True
    )

    # About Section
    st.subheader("About Us")
    about_content = """
        <p style="text-align: justify;">
            Automobile loans have become essential for personal and business transportation, with many individuals and businesses relying on Non-Banking Financial Institutions (NBFIs) for financing. NBFIs are increasingly popular due to their tailored solutions for various financial situations, attracting a diverse range of applicants with lower credit standards and shorter loan terms compared to traditional banks. They play a crucial role in the economy by serving clients who might struggle to obtain loans from conventional banks, including those with less-than-perfect credit histories or those seeking quick financing.
            However, the accessibility of NBFIs can lead to higher default risks. Defaults on automobile loans may arise from factors such as job loss, illness, or unexpected financial hardships that hinder timely payments. Clients may also take on multiple loans without fully understanding their repayment obligations, and poor financial management can further exacerbate defaults. Economic conditions, such as recessions or inflation, may leave borrowers with reduced disposable income, making it challenging to meet loan commitments. Understanding these dynamics is essential for both borrowers and lenders navigating the complexities of automobile financing today.
        </p>
    """

    # Create a two-column layout for the About section
    col1, col2, col3 = st.columns([2.5, 0.1, 1.5])

    with col1:
        st.markdown(about_content, unsafe_allow_html=True)

    with col3:
        st.image("static/loan.jpg", use_column_width=True)

    st.markdown(
        """
        </br><hr style="border: 3px solid #FFDF00; width: 100%; margin: auto; border-radius: 50px">
        """,
        unsafe_allow_html=True
    )


    # Expander to show/hide the Terms and Conditions content
    col1, col2, col3 = st.columns([2.5, 0.1,  1.5])
    with col1:
        st.markdown("""
            <div style='background-color: #FAFAD2; padding: 0px; width: 100%; border-radius: 0px;'>
                <h4 style='margin: 0;position: relative;left:20px'>Terms and Conditions</h4>
            </div></br>
        """, unsafe_allow_html=True)

        st.markdown("""
            ##### 1. Use of the System:
            The system provides information and predictions based on user input and is not responsible for financial decisions made from these predictions.

            ##### 2. User Responsibilities:
            Users must provide accurate and complete information, as the system is not liable for errors caused by misuse or incorrect data.

            ##### 3. Data Privacy:
            User data will be kept private and not shared with third parties without consent, except as required by law.

            ##### 4. Liability Disclaimer:
            The system does not guarantee prediction accuracy or reliability, and users assume all risks associated with its use.

            ##### 5. Modifications to the Terms:
            The terms may be updated at any time without notice, and continued use of the system indicates acceptance of any changes.
        """)

    with col3:
        st.markdown("""
                <div style='background-color: #FAFAD2; padding: 0px; width: 100%; border-radius: 0px; position: relative;left:-10px'>
                <h4 style='margin: 0;position: relative;left:20px'>Feedback</h4>
            </div></br>
                If you have any questions, feedback, or concerns, please fill out the form below, and we will get back to you as soon as possible.</br></br>
        """, unsafe_allow_html=True)

        # Contact form
        with st.form(key='contact_form'):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Your Message")

            submit_button = st.form_submit_button(label='Submit')

            if submit_button:
                # Process the form data
                if name and email and message:
                    st.success("Thank you for your message! We will get back to you soon.")
                else:
                    st.error("Please fill out all fields.")

    st.markdown(
        """
        <hr style="border: 3px solid #FFDF00; width: 100%; margin: auto; border-radius: 50px">
        """,
        unsafe_allow_html=True
    )

    # Testimonials Section
    st.subheader("What People Say")

    # Testimonials data with 4 entries
    testimonials = [
        ("John Doe", "This app has completely transformed the way I assess loan risks. Highly recommended!"),
        ("Jane Smith", "An essential tool for any lender. The predictions are spot on!"),
        ("Bob Johnson", "A user-friendly interface and accurate predictions. Fantastic work!"),
        ("Alice Brown", "Incredible accuracy and easy to use. My go-to for loan assessments!")
    ]

    # Loop through the testimonials and display them one by one
    for name, testimonial in testimonials:
        st.markdown(
            f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 15px; margin: 10px 0; 
                         background-color: #f9f9f9; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <strong style="color: #333; font-size: 1.1em;">{name}</strong>: 
                <span style="color: #555; font-size: 1em;">{testimonial}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Card style
    st.markdown(
        """
        <style>
            .contact-card {
                background-color: #FAFAD2;  /* Card background color */
                border-radius: 50px; 
                padding: 20px;  
                width: 100%;  
                height: auto; 
                margin: auto; 
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
            }
            .contact-card ul {
                list-style-type: none;  /* Remove bullets */
                padding: 0;  /* Remove padding */
                margin: 0;  /* Remove margin */
            }
        </style>
        </br>  
        <div class="contact-card">
            <h2>Contact Us</h2>
            <p>
                If you have any questions or inquiries, feel free to reach out to us at:
                <ul>
                    <li><strong>Email : </strong> support@loansystem.com</li>
                    <li><strong>Phone : </strong> +1 (123) 456-7890</li>
                    <li><strong>Address : </strong> 123 Loan St, Malabe, Sri Lanka</li>
                </ul>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Footer style
    st.markdown(
        """
        <style>
            .footer {
                border-top: 1px solid #ccc;
                padding: 20px; 
                text-align: center; 
                position: relative; 
                bottom: 0; 
                width: 100%; 
            }
            .footer img {
                width: 30px;
                height: auto; 
                margin: 0 10px; 
            }
            .footer .company-logo {
                width: 100px; /* Adjust logo size */
                height: auto; 
                margin-bottom: 10px;
            }
        </style>

        <div class="footer">
            <p>&copy; 2024 Automobile Loan Default Prediction System by Mining Minds. All rights reserved.</p>
            <p>
                Follow us on 
                <a href="https://twitter.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg" alt="Twitter Logo">
                </a>
                <a href="https://facebook.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook Logo">
                </a>
                <a href="https://instagram.com" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram Logo">
                </a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


with tab2:
    # Add custom CSS for form width
    st.markdown(
        """
        <style>
        .form-container {
            max-width: 100px;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Container for form
    st.markdown(
        """
        <style>
        .form-container {
            max-width: 600px;  /* Set the max width for the entire form */
            position: absolute;
            left:100px;
        }
        .stNumberInput, .stSelectbox, .stTextInput {
            max-width: 600px;  /* Set the max width for input fields */
        }
        </style>
        """, unsafe_allow_html=True
    )


    with st.container():
        # Add custom CSS for form width
        st.markdown(
            """
            <style>
            .form-container {
                max-width: 100px;
            }
            </style>
            """, unsafe_allow_html=True
        )

        # Add a new image that covers the full area of the prediction form
        st.image("static/topup.jpg",
                 use_column_width=True,
                 caption="Full Area Vehicle Loan Default Prediction", output_format='auto')

        st.markdown('<div class="form-container">', unsafe_allow_html=True)  # Start form container

        # Section: Personal Details
        st.header("Personal Details")
        st.markdown(
            """
            <hr style="border: 3px solid #FFDF00; width: 100%; margin: auto; border-radius: 50px">
            """,
            unsafe_allow_html=True
        )

        # Create two columns for personal details
        col1, col2 = st.columns(2)

        with col1:
            Client_Education = st.selectbox('Client Education', ['Graduation', 'Secondary', 'Other'])
            Client_Gender = st.selectbox('Client Gender', ['Male', 'Female', 'Other'])
            age_years = st.number_input('Age in Years', min_value=0, value=0)
            Age_Days = age_years * 365
            Client_Marital_Status = st.selectbox('Client Marital Status', ['Married', 'Single', 'Divorced', 'Widow', 'Other'])
            ID_Days = st.number_input('Days Since Document Change', min_value=0, value=0)
            Client_Housing_Type = st.selectbox('Client Housing Type', ['Home', 'Family', 'Municipal', 'Other'])
            Client_Family_Members = st.number_input('Number of Family Members', min_value=0, value=0)

        with col2:
            Client_Income_Type = st.selectbox('Client Income Type', ['Service', 'Commercial', 'Retired', 'Govt Job', 'Other'])
            Client_Permanent_Match_Tag = st.selectbox('Contact and Permanent Address Match', ['Yes', 'No'])
            Mobile_Tag = st.selectbox('Client Mobile Number', ['Yes', 'No'])
            Car_Owned = st.selectbox('Car Owned', ['Yes', 'No'])
            Bike_Owned = st.selectbox('Bike Owned', ['Yes', 'No'])
            Active_Loan = st.selectbox('Active Loan', ['Yes', 'No'])
            House_Own = st.selectbox('House Owned', ['Yes', 'No'])

        # Section: Financial Details
        st.header("Financial Details")
        st.markdown(
            """
            <hr style="border: 3px solid #FFDF00; width: 100%; margin: auto; border-radius: 50px">
            """,
            unsafe_allow_html=True
        )

        # Create two columns for financial details
        col3, col4 = st.columns(2)

        with col3:
            Client_Income = st.number_input('Client Income', min_value=0, value=0)
            Credit_Amount = st.number_input('Credit Amount', min_value=0, value=0)

        with col4:
            Loan_Contract_Type = st.selectbox('Loan Contract Type', ['Cash loans', 'Revolving loans', 'Other'])

        # Combine the inputs into a single DataFrame for scaling
        input_scaler_data = pd.DataFrame({
            'Client_Income': [Client_Income],
            'Credit_Amount': [Credit_Amount],
            'Age_Days': [Age_Days],
            'ID_Days': [ID_Days]
        })

        # Scale the data
        scaler = StandardScaler()
        scaled_values = scaler.fit_transform(input_scaler_data)

        # Assign the scaled values to the respective variables
        Client_Incomes = scaled_values[0][0]
        Credit_Amounts = scaled_values[0][1]
        Age_Dayss = scaled_values[0][2]
        ID_Dayss = scaled_values[0][3]

        # Create input data as a dataframe
        input_data = pd.DataFrame({
            'Client_Income': [scaled_values[0][0]],
            'Car_Owned': [Car_Owned],
            'Bike_Owned': [Bike_Owned],
            'Active_Loan': [Active_Loan],
            'House_Own': [House_Own],
            'Credit_Amount': [scaled_values[0][1]],
            'Client_Income_Type': [Client_Income_Type],
            'Client_Education': [Client_Education],
            'Client_Marital_Status': [Client_Marital_Status],
            'Client_Gender': [Client_Gender],
            'Loan_Contract_Type': [Loan_Contract_Type],
            'Client_Housing_Type': [Client_Housing_Type],
            'Age_Days': [scaled_values[0][2]],
            'ID_Days': [scaled_values[0][3]],
            'Mobile_Tag': [Mobile_Tag],
            'Client_Family_Members': [Client_Family_Members],
        })

        # Encode categorical variables based on predefined mappings
        encode_map = {
            'Client_Income_Type': {'Service': 0, 'Commercial': 1, 'Retired': 2, 'Govt Job': 3, 'Other': 99},
            'Client_Education': {'Graduation': 1, 'Secondary': 0, 'Other': 99},
            'Client_Marital_Status': {'Married': 0, 'Single': 1, 'Divorced': 2, 'Widow': 3, 'Other': 99},
            'Client_Gender': {'Male': 0, 'Female': 1, 'Other': 99},
            'Loan_Contract_Type': {'Cash loans': 0, 'Revolving loans': 1, 'Other': 99},
            'Client_Housing_Type': {'Home': 0, 'Family': 1, 'Municipal': 2, 'Other': 99},
            'Client_Permanent_Match_Tag': {'Yes': 1, 'No': 0},
            'Car_Owned': {'Yes': 1, 'No': 0},
            'Bike_Owned': {'Yes': 1, 'No': 0},
            'Active_Loan': {'Yes': 1, 'No': 0},
            'House_Own': {'Yes': 1, 'No': 0},
            'Mobile_Tag': {'Yes': 1, 'No': 0},
        }

        # Apply encoding to categorical columns
        input_data['Client_Income_Type'] = encode_map['Client_Income_Type'][Client_Income_Type]
        input_data['Client_Education'] = encode_map['Client_Education'][Client_Education]
        input_data['Client_Marital_Status'] = encode_map['Client_Marital_Status'][Client_Marital_Status]
        input_data['Client_Gender'] = encode_map['Client_Gender'][Client_Gender]
        input_data['Loan_Contract_Type'] = encode_map['Loan_Contract_Type'][Loan_Contract_Type]
        input_data['Client_Housing_Type'] = encode_map['Client_Housing_Type'][Client_Housing_Type]
        input_data['Client_Permanent_Match_Tag'] = encode_map['Client_Permanent_Match_Tag'][Client_Permanent_Match_Tag]
        input_data['Car_Owned'] = encode_map['Car_Owned'][Car_Owned]
        input_data['Bike_Owned'] = encode_map['Bike_Owned'][Bike_Owned]
        input_data['Active_Loan'] = encode_map['Active_Loan'][Active_Loan]
        input_data['House_Own'] = encode_map['House_Own'][House_Own]
        input_data['Mobile_Tag'] = encode_map['Mobile_Tag'][Mobile_Tag]

        # When the user clicks the Predict button
        if st.button('Predict Loan Default'):
            # Call the backend function to predict using the app.py function
            prediction = app.predict_loan_default(input_data)

            # Display the result
            if prediction == 1:
                st.error('Prediction: High Risk of Loan Default')
            else:
                st.success('Prediction: Low Risk of Loan Default')

        st.markdown('</div>', unsafe_allow_html=True)
