# Importing all the required libraries
import PySimpleGUI as sg  # For Graphical User Interface
import validate  # Custom Library
import PopulateDatabase as pd  # Custom Library


# This is the User Interface for the Librarian Page
def librarian_page():
    # Each layout here is a tab in the librarian window
    tab1_layout = [[sg.Text('Name of the book', grab=True), sg.Input(key='bookname',
                                                                     tooltip='Enter the name of the book')],
                   [sg.Text('Book Author', grab=True), sg.Input(key='author', tooltip='Enter the author of the book')],
                   [sg.Text('Quantity', grab=True), sg.Input(key='qty',
                                                             tooltip='Enter the number of books you want to buy')],
                   [sg.Text('Price', grab=True), sg.Input(key='price', tooltip='Enter the price of the book')],
                   [sg.Button('Add', key='add'), sg.Button('Cancel', key='cancel')]]

    tab2_layout = [[sg.Text('Name of the book', grab=True), sg.Input(key='bookname1', tooltip='Enter the book name')],
                   [sg.Text('Author of the book', grab=True), sg.Input(key='author1',
                                                                       tooltip="Enter the author of the book")],
                   [sg.Text('No of books'), sg.Input(key='qty1', tooltip='Enter the number of books')],
                   [sg.Button('Delete', key='delete'), sg.Button('Cancel', key='cancel1')]]

    tab3_layout = [[sg.Text('Name of the book', grab=True), sg.Input(key='bookname2', tooltip='Enter the book name')],
                   [sg.Text('Author of the book', grab=True), sg.Input(key='author2', tooltip='Enter the author')],
                   [sg.Button('Modify', key='modify'), sg.Button('Cancel', key='cancel2')]]

    tab4_layout = [[sg.Text('Name of the book', grab=True), sg.Input(key='bookname3', tooltip='Enter the book name')],
                   [sg.Text('Author', grab=True), sg.Input(key='author3', tooltip='Enter the author')],
                   [sg.Text('Number of books', grab=True), sg.Slider(range=(0, 40), orientation='h', key='qty3')],
                   [sg.Button('Lend', key='lend'), sg.Button('Cancel', key='cancel3')]]

    layout = [[sg.TabGroup([[sg.Tab('Add', tab1_layout), sg.Tab('Delete', tab2_layout),
                             sg.Tab('Modify', tab3_layout), sg.Tab('Lend', tab4_layout)]])]]

    modify_layout = [[sg.Text('Name', grab=True), sg.Input(key='mname', tooltip='Modified Book Name')],
                     [sg.Text('Author', grab=True), sg.Input(key='mauthor', tooltip='Modified Author')],
                     [sg.Text('Quantity', grab=True), sg.Input(key='mqty', tooltip='Modified quantity')],
                     [sg.Text('Price', grab=True), sg.Input(key='mprice', tooltip='Modified Price')],
                     [sg.Button('Modify', key='m-modify'), sg.Button('Cancel', key='mcancel')]]

    window = sg.Window('WELCOME', layout)

    # event loop for the librarian window
    while True:
        event, values = window.read()
        print(event, values)
        # tab = window.Element('add').GetCurrent()
        if event in (sg.WIN_CLOSED, 'cancel', 'cancel1', 'cancel2', 'cancel3'):
            break

        elif event == 'add':
            pd.populate_new_book(values['bookname'], values['author'], int(values['qty']), float(values['price']))
            break

        elif event == 'delete':
            pd.delete_from_book(values['bookname1'])
            break

        elif event == 'modify':
            if validate.book_exists(values['bookname2'], values['author2']):
                window.close()
                modification_window = sg.Window('Modify Details', modify_layout)

                while True:
                    m_event, m_values = modification_window.read()
                    if m_event in (sg.WIN_CLOSED, 'mcancel'):
                        break
                    elif m_event == 'm-modify':
                        pd.modify_book(m_values['mname'], m_values['mauthor'], m_values['mqty'], m_values['mprice'],
                                       values['bookname2'], values['author2'])
                        modification_window.close()
                        break

                modification_window.close()

            else:
                sg.Popup('Book does not exist')

        elif event == 'lend':
            pd.lend_book(values['bookname3'], values['author3'], int(values['qty3']))
            break

    # Always close the window
    window.close()


# Main page that anyone sees when first opening the application
def home_page():
    users = ['Librarian', 'Customer']
    sex = ['M', 'F', 'O']

    sg.theme('DarkBlue3')

    # Defining each layout before defining the window and the loop for each column
    main_layout = [[sg.Text('WELCOME', justification='center', size=(80, 2), grab=True)],
                   [sg.Text('Nothing is pleasanter than exploring a library', justification='center', size=(80, 1),
                            grab=True, tooltip='True')],
                   [sg.Text('Are you a Customer or a Librarian? ', grab=True, tooltip='Required')],
                   [sg.R(text, 1, size=(18, 12), auto_size_text=True, tooltip=text, key=text) for text in users],
                   [sg.Button('Confirm', key='mconfirm'), sg.Button('Cancel', key='mcancel')]]

    customer_layout = [[sg.Frame('Customer Sign In', [[]])],
                       [sg.Text('Name', grab=True, tooltip='Type your name'), sg.Input(key='cname')],
                       [sg.Text('Password', grab=True, tooltip='test'), sg.Input(key='cpass', password_char='*')],
                       [sg.Button('Sign In', key='cconfirm', bind_return_key=True), sg.Button('Exit', key='cexit')],
                       [sg.Text("Don't have an account?"), sg.Button('Sign Up', enable_events=True, key='clink')],
                       [sg.Button('Forgot Password', key='cfpass')]]

    librarian_layout = [[sg.Frame('Librarian Sign In', [[]])],
                        [sg.Text('Name', grab=True), sg.Input(key='lname', tooltip='Type your name here')],
                        [sg.Text('Password', grab=True),
                         sg.Input(key='lpass', tooltip='Type your password here', password_char='*')],
                        [sg.Button('Sign In', key='lconfirm'), sg.Button('Cancel', key='lcancel')],
                        [sg.Button('Forgot Password', key='libFpass')]]

    customer_signup_layout = [[sg.Frame('Sign Up', [[]])],
                              [sg.Text('WELCOME', grab=True, justification='center', size=(60, 2))],
                              [sg.Text('Name', grab=True), sg.Input(key='newname', tooltip='Type your name here')],
                              [sg.Text('Age', grab=True), sg.Input(key='newage', tooltip='Type your age here')],
                              [sg.Text('Sex', grab=True)],
                              [sg.R(s, 1, auto_size_text=True, tooltip=s, key=s) for s in sex],
                              [sg.Text('City', grab=True), sg.Input(key='newcity', tooltip='Type your city here')],
                              [sg.Text('Password', grab=True),
                               sg.Input(key='newpass', tooltip='Type your password here',
                                        password_char='*')],
                              [sg.Text('Confirm Password', grab=True), sg.Input(key='newpass1',
                                                                                tooltip='Type your password again',
                                                                                password_char='*')],
                              [sg.Button('Create Account', key='create'), sg.Button('Cancel', key='cscancel')]]

    librarian_forgot_password_layout = [[sg.Frame('Recover', [[]], size=(40, 1))],
                                        [sg.Text('Name', grab=True), sg.Input(key='fpname',
                                                                              tooltip='Type your name here')],
                                        [sg.Text('Age', grab=True),
                                         sg.Input(key='fpage', tooltip='Type your age here')],
                                        [sg.Text('Sex', grab=True)],
                                        [sg.R(s, 1, auto_size_text=True, tooltip=s, key=s+s) for s in sex],
                                        [sg.Text('City', grab=True), sg.Input(key='fpcity',
                                                                              tooltip='Type your city here')],
                                        [sg.Button('Find', key='fpfind'), sg.Button('Cancel', key='fpcancel')]]

    change_librarian_password_layout = [[sg.Text('New Password', grab=True), sg.Input(key='cppass',
                                                                                      tooltip='Enter your password',
                                                                                      password_char='*')],
                                        [sg.Text('Confirm Password', grab=True), sg.Input(key='cppass1',
                                                                                          password_char='*',
                                                                                          tooltip='Confirm password')],
                                        [sg.Button('Confirm', key='cpconfirm'), sg.Button('Cancel', key='cpcancel')]]

    # librarian_function_layout = [[]]

    final_layout = [[sg.Column(main_layout, key='layout1'),
                     sg.Column(customer_layout, key='layout2', visible=False),
                     sg.Column(librarian_layout, key='layout3', visible=False),
                     sg.Column(customer_signup_layout, key='layout4', visible=False),
                     sg.Column(librarian_forgot_password_layout, key='layout5', visible=False),
                     sg.Column(change_librarian_password_layout, key='layout6', visible=False)]]

    window = sg.Window('Welcome to the Library', final_layout)

    while True:
        event, values = window.read()
        if event == 'mcancel' or event == sg.WIN_CLOSED:
            break
        elif event == 'mconfirm':
            if values['Librarian']:
                window['layout1'].update(visible=False)
                window['layout3'].update(visible=True)
                while True:
                    lib_events, lib_values = window.read()
                    if lib_events == 'lcancel' or lib_events == sg.WIN_CLOSED:
                        window['layout3'].update(visible=False)
                        window['layout1'].update(visible=True)
                        break
                    elif lib_events == 'lconfirm':
                        if validate.check_librarian(lib_values['lname'], lib_values['lpass']):
                            # window['layout3'].update(visible=False)
                            # window['layout1'].update(visible=True)
                            window.close()
                            librarian_page()
                            break
                        else:
                            sg.Popup('Librarian not found')
                            window['layout3'].update(visible=False)
                            window['layout3'].update(visible=True)
                    elif lib_events == 'libFpass':
                        window['layout3'].update(visible=False)
                        window['layout5'].update(visible=True)
                        while True:
                            fpevent, fpvalues = window.read()
                            fpvalues['fpage'] = int(fpvalues['fpage'])
                            if fpevent == 'fpcancel' or fpevent == sg.WIN_CLOSED:
                                break
                            elif fpevent == 'fpfind':
                                if validate.find_librarian(fpvalues['fpname'], fpvalues['fpage'], fpvalues['fpcity']):
                                    window['layout5'].update(visible=False)
                                    window['layout6'].update(visible=True)
                                    while True:
                                        cpevent, cpvalues = window.read()
                                        if cpevent == 'cpcancel' or cpevent == sg.WIN_CLOSED:
                                            break
                                        elif cpevent == 'cpconfirm':
                                            if validate.check_password(cpvalues['cppass'], cpvalues['cppass1']):
                                                pd.change_librarian_password(fpvalues['fpname'], fpvalues['fpage'],
                                                                             fpvalues['fpcity'], cpvalues['cppass'])
                                                sg.Popup('Succesfully Changed password')
                                                break
                                            else:
                                                break
                                    break
                                else:
                                    break
                        break
            elif values['Customer']:
                window['layout1'].update(visible=False)
                window['layout2'].update(visible=True)
                while True:
                    cusevent, cusvalues = window.read()
                    if cusevent == 'cexit' or cusevent == sg.WIN_CLOSED:
                        break
                    elif cusevent == 'clink':  # Sign Up
                        window['layout2'].update(visible=False)
                        window['layout4'].update(visible=True)
                        while True:  # Sign Up Event loop
                            csevent, csvalues = window.read()
                            csvalues['newage'] = int(csvalues['newage'])
                            if csevent == 'cscancel' or csevent == sg.WIN_CLOSED:
                                break
                            elif csevent == 'create':
                                if csvalues['M']:
                                    if validate.check_password(csvalues['newpass'], csvalues['newpass1']):
                                        pd.populate_new_customer(csvalues['newname'], csvalues['newage'], 'M',
                                                                 csvalues['newcity'], csvalues['newpass'])
                                        break
                                    else:
                                        sg.Popup('Password does not match')
                                elif csvalues['F']:
                                    if validate.check_password(csvalues['newpass'], csvalues['newpass1']):
                                        pd.populate_new_customer(csvalues['newname'], csvalues['newage'], 'F',
                                                                 csvalues['newcity'], csvalues['newpass'])
                                        break
                                    else:
                                        sg.Popup('Password does not match')
                                elif csvalues['O']:
                                    if validate.check_password(csvalues['newpass'], csvalues['newpass1']):
                                        pd.populate_new_customer(csvalues['newname'], csvalues['newage'], 'O',
                                                                 csvalues['newcity'], csvalues['newpass'])
                                        break
                                    else:
                                        sg.Popup('Password does not match')

        break

    window.close()
