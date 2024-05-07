from auto_download_undetected_chromedriver import download_undetected_chromedriver

folder_path = "D:\\Projects\\Projects_Cobrance\\Search Linkedin\\drivers"
chromedriver_path = download_undetected_chromedriver(
    folder_path, undetected=True, arm=False, force_update=True
)