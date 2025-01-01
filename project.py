import streamlit as st

# Sample data for College Info (Images & Links)
college_images = [
    {
        "name": "Government Post Graduate College",
        "image": "https://lh3.googleusercontent.com/p/AF1QipMlwJFBzv2rsql-kzOZ0JcISn5eVt6SxvWE5NbW=s680-w680-h510",
        "url": "https://www.google.com/search?q=post+graduate+college+charsadda&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCEC4YJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgYIBxBFGEDSAQk0MTc0OWowajeoAgewAgE&sourceid=chrome&ie=UTF-8#lpg=cid:CgIgAQ%3D%3D,ik:CAoSLEFGMVFpcE1sd0pGQnp2MnJzcWwta3pPWjBKY0lTbjVlVnQ2U3h2V0U1TmJX"
    },
]

# Function to display college images and links
def display_college_info():
    st.title("Government Post Graduate College")
    st.write("""
    **Welcome to the Government Post Graduate College's Application Portal**. 
    We are excited to have you apply for the **BS Programming** program for the year 2025.
    Please fill out the form below with your personal and academic details.
    """)

    # Display college images with links
    for college in college_images:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.image(college['image'], use_column_width=True)
        with col2:
            st.write(f"[{college['name']}]({college['url']})")

# Function to create the application form
def application_form():
    st.header("BS Programming - Application Form (2025)")

    # Form Fields
    with st.form("application_form"):
        # Personal Information
        st.subheader("Personal Information")
        full_name = st.text_input("Full Name")
        father_name = st.text_input("Father's Name")
        dob = st.date_input("Date of Birth")
        nationality = st.text_input("Nationality")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        
        # Address Information
        st.subheader("Address Information")
        permanent_address = st.text_area("Permanent Address")
        current_address = st.text_area("Current Address")
        
        # Educational Background
        st.subheader("Educational Background")
        matric_school = st.text_input("Matriculation School Name")
        matric_year = st.number_input("Matriculation Year", min_value=2000, max_value=2025, step=1)
        intermediate_college = st.text_input("Intermediate College Name")
        intermediate_year = st.number_input("Intermediate Year", min_value=2000, max_value=2025, step=1)
        intermediate_percentage = st.number_input("Intermediate Percentage", min_value=0, max_value=100)
        
        # Additional Information
        st.subheader("Additional Information")
        extra_curricular = st.text_area("Extra-curricular Activities")
        personal_statement = st.text_area("Personal Statement (Why do you want to join BS Programming?)")
        
        # Upload Documents (Optional)
        st.subheader("Document Uploads")
        transcript = st.file_uploader("Upload Transcript", type=["pdf", "jpg", "jpeg", "png"])
        id_card = st.file_uploader("Upload ID Card", type=["jpg", "jpeg", "png", "pdf"])
        
        # Submit Button
        submit_button = st.form_submit_button("Submit Application")

        if submit_button:
            st.success("Your application has been successfully submitted. We will get back to you soon.")

# Main Application
def main():
    # Display college info (images and links)
    display_college_info()

    # Show the application form
    application_form()

if __name__ == "__main__":
    main()
