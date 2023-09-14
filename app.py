import pymysql
import streamlit as st
import connectmysql as con

# create DB connection
connection = con.connectdb()
cursor = connection.cursor()

st.title('MySQL person CRUD app')

# Func อ่านข้อมูลจากตาราง person ใน mysql database


def read_persons():
    cursor.execute("SELECT * FROM person")
    persons = cursor.fetchall()
    return persons

# Function Insert data in to PERSON


def insert_persons(fullname, email, age):
    try:
        # SQL insert new row
        cursor.execute(
            "INSERT INTO person(fullname, email, age) VALUES(%s,%s,%s)",
            (fullname, email, age)
        )
        connection.commit()
        st.success("INSERT data success")
        # Redirect to Read page
        st.markdown("Click [link](?menu=Read) to view person data")
        st.markdown("""
            <a href="?menu=Read" target="_self">Click here</a> to view person data
        """, unsafe_allow_html=True)
    except pymysql.Error:
        connection.rollback()
        st.error(f"Error CAN NOT insert data !!!")


def update_persons(id, fullname="", email="", age=0):
    try:
        # SQL insert new row
        cursor.execute(
            "UPDATE person SET fullname=%s, email=%s, age=%s WHERE id = %s",
            (fullname, email, age, id)
        )
        connection.commit()
        st.success("UPDATE data success")
    except pymysql.Error:
        connection.rollback()
        st.error(f"Error CAN NOT update data !!!")


def delete_persons(id):
    try:
        # SQL insert new row
        cursor.execute(
            "DELETE FROM person WHERE id = %s",
            (id)
        )
        connection.commit()
        st.success("DELETE data success")
    except pymysql.Error:
        connection.rollback()
        st.error(f"Error CAN NOT delete data !!!")


# ---------------------------------------------------------------------------
# Main menu
menu = st.sidebar.selectbox("Menu", ["Read", "Create", "Update", "Delete"])

# Menu : Read
if menu == "Read":
    st.subheader("Read Person")
    persons = read_persons()
    # check persons is not empty

    if persons:
        # Table header
        table_data = [["ID", "Fullname", "Email", "Age", "Setting"]]

        for person in persons:
            link_edit = f"[Edit {person['id']}]"
            link_delete = f"[Delete {person['id']}]"
            row = [person['id'], person['fullname'],
                   person['email'], person['age'], link_edit, link_delete]

            table_data.append(row)

        st.table(table_data)
    else:
        st.info("ไม่มีข้อมูลใน DB")

# Menu Create
elif menu == "Create":
    st.subheader("Create Person")
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.text_input("Age", 0, 100, 1)

    # Button clicked
    if st.button("Create"):
        # check input data not empty
        if fullname and email and age:
            # SQL insert new row
            insert_persons(fullname, email, age)
        else:
            st.warning("กรอกข้อมูลให้ครบถ้วน")

# Menu update
elif menu == "Update":
    st.subheader("Update Person")
    id = st.number_input("ID", min_value=1)
    fullname = st.text_input("Fullname")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=1, max_value=100)

    if st.button("Update"):
        update_persons(id, fullname, email, age)

# Menu delete
elif menu == "Delete":
    st.subheader("Delete Person")
    id = st.number_input("ID", min_value=1)

    if st.button("Delete"):
        delete_persons(id)
