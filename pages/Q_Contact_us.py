from Analysis import st


st.set_page_config(page_title="Contact Us",
                   page_icon="✊")

st.markdown(
        """
        <div style="background-color:#025246 ;padding:5px">
        <h2 style="color:white;text-align:center;">Contact Us</h2>
        </div>
        """,
        unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    <h1 style="text-align:center"> BHARGAVESH DAKKA </h1>
    <p style="text-align:center"> Gmail : bhargaveshdakka@gmail.com</p>
    <h6 style="text-align:center; color:red"> Social Profiles </h6>
    """,unsafe_allow_html=True
)



def main():
    st.markdown("""
    <center>
    <style>.container { display: inline-flex; flex-direction: row; align : center; }</style>
    <div class='container'>
    <div class='item' style='width: 50px; height: 50px; background-color: #e2e2e2; margin-right: 10px;'>
        <a href = "https://github.com/bhargavesh-dakka">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub" width="50" height="50">        
        </a>
    </div> 
    <div class='item' style='width: 50px; height: 50px; background-color: #e2e2e2; margin-right: 10px;'>
        <a href = "https://www.linkedin.com/in/bhargavesh-dakka/">
            <img src="https://www.practicepanther.com/wp-content/uploads/2016/06/linkedin-for-lawyers.png", alt = "LinkedIn", width = "50" height = "50">
        </a>
    </div>
    </center>
    
    """,unsafe_allow_html=True)

main()