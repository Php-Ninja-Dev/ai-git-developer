
import ftplib


def download_ftp_folder(sandbox: Sandbox, args: Dict[str, Any]) -> str:
    ftp_server = args['ftp_server']
    ftp_path = args['ftp_path']
    local_path = args['local_path']
    username = args.get('username')
    password = args.get('password')

    print_sandbox_action('Downloading FTP folder', f"{ftp_path} to {local_path}")

    try:
        with ftplib.FTP(ftp_server) as ftp:
            if username and password:
                ftp.login(username, password)
            else:
                ftp.login()

            filenames = ftp.nlst(ftp_path)
            sandbox.filesystem.make_dir(local_path)

            for filename in filenames:
                local_filepath = os.path.join(local_path, os.path.basename(filename))
                with open(local_filepath, 'wb') as f:
                    ftp.retrbinary('RETR ' + filename, f.write)

        return 'success'
    except ftplib.all_errors as e:
        return f"FTP error: {e}"
    except Exception as e:
        return f"Error: {e}"
