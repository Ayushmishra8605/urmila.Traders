import streamlit as st
from pdf_utils import download_button_logic
from style import STYLE
st.markdown(STYLE,unsafe_allow_html=True)
st.sidebar.markdown("developer: Ayush mishra")
st.title("Welcome to Urmila traders")
# 1. Initialize session State (Ye check karein ki ye sahi se likha hai)
if 'items_list' not in st.session_state:
    st.session_state.items_list = []  # Naam badal kar 'items_list' kar diya taaki confusion na ho

if 'customer_name' not in st.session_state:
    st.session_state.customer_name = ""
st.title("Billing System")
with st.expander("calculator"):
# Customer Name
    name_input = st.text_input("Enter customer name:", value=st.session_state.customer_name)
    st.session_state.customer_name = name_input
     # Input
    col1, col2,col3 = st.columns(3)
    with col1:
        amount = st.number_input("Enter amount:", min_value=0,key="current_amt")
    with col2:
        quantity = st.number_input("Enter quantity:", min_value=0,key="quantity")
        unit= st.radio("Select unit:", ["kg","L","Pcs"],horizontal=True)
    with col3:
        pname= st.text_input("Enter product name:",key="pname")
# Add Item Button
    if st.button("Add Item"):
        if  pname and amount > 0 and quantity > 0:
        # List mein item add karna
            st.session_state.items_list.append({"name":pname,"amount": amount,"quantity": quantity,"unit":unit})
            st.success("Item Added!")
# Bill Display (Yahan Error aa raha tha)
        if st.session_state.items_list:
            st.markdown("---")
            st.write(f"### Bill for: {st.session_state.customer_name} ")
            total=0
                     # Loop over the LIST (not the method)#
            for i, item in enumerate(st.session_state.items_list):
                item_total = item['amount'] * item['quantity']
                total+= item_total
                st.text(f"Item {i + 1}:{item['name']} {item['amount']} x {item['quantity']} = {item_total}")
            st.header(f"Total: ₹{total}")
            download_button_logic(
                st.session_state.items_list,
                st.session_state.customer_name)
            if  st.button("New customer/Reset"):
                st.session_state.items_list=[]
                st.session_state.customer_name = ""
                st.rerun()
st.sidebar.markdown("....")
st.sidebar.subheader(" connect with me on Social media ")
st.sidebar.link_button("Instagram","https://instagram.com/bantimishra13")
st.sidebar.link_button("Youtube","https://youtube.com/yuva_e_jaunpur_ayush_18")
st.sidebar.link_button("facebook","https://www.facebook.com/share/1KNUwJro3c/")
st.sidebar.link_button("whatsapp","https://wa.me/918756085720")
st.sidebar.subheader("Thanks you for visiting us")

st.sidebar.subheader("Welcome to our Digital Space! 🚀 > Connect with us on Facebook for the latest updates, behind-the-scenes, and much more. Click the link below to join our community!")
