import os
import datetime
import csv
import codecs
import shutil
import magic

from scripts.artifact_report import ArtifactHtmlReport
from scripts.ilapfuncs import logfunc, tsv, timeline, is_platform_windows, snapchat_month

def get_snapchatReturn(files_found, report_folder, seeker, wrap_text):
    
    for file_found in files_found:
        file_found = str(file_found)
        
        filename = os.path.basename(file_found)
        
        if filename.startswith('subscriber_information.csv'):
            data_list =[]
            with open(file_found, 'r') as f:
                delimited = csv.reader(f, delimiter=',')
                
                x = range(4)
                for n in x:
                    next(delimited)
                for item in delimited:
                
                    user_id = item[0]
                    email_address = item[1]
                    created = item[2]
                    creation_ip = item[3]
                    phone_number = item[4]
                    display_name = item[5]
                    status = item[6]
                    #Split timestamp date and time
                    split_timestamp = created.split(' ')
                    numeric = snapchat_month(split_timestamp[1])
                    clean_timestamp = f'{split_timestamp[-1]}-{numeric}-{split_timestamp[2]} {split_timestamp[3]}'
                    data_list.append((clean_timestamp, user_id, email_address, creation_ip, phone_number, display_name, status))
                
                
            if data_list:
                report = ArtifactHtmlReport('Snapchat - Return')
                report.start_artifact_report(report_folder, 'Snapchat - Subscriber Info')
                report.add_script()
                data_headers = ('Date Created (UTC)', 'ID', 'Email Address', 'Creation IP', 'Phone Number', 'Display Name', 'Status' )
                report.write_artifact_data_table(data_headers, data_list, file_found)
                report.end_artifact_report()
                
                tsvname = f'Snapchat - Subscriber Info'
                tsv(report_folder, data_headers, data_list, tsvname)
                
                #tlactivity = f'Kik - bind'
                #timeline(report_folder, tlactivity, data_list, data_headers)
            else:
                logfunc('No Snapchat - Subscriber Info data available')
                
        if filename.startswith('ip_data.csv'):
            data_list =[]
            with open(file_found, 'r') as f:
                    delimited = csv.reader(f, delimiter=',')
                    
                    x = range(4)
                    for n in x:
                        next(delimited)
                    for item in delimited:
                        
                        ip = item[0]
                        type = item[1]
                        timestamp = item[2]
                        #Split timestamp date and time
                        split_timestamp = timestamp.split(' ')
                        numeric = snapchat_month(split_timestamp[1])
                        clean_timestamp = f'{split_timestamp[-1]}-{numeric}-{split_timestamp[2]} {split_timestamp[3]}'
                        data_list.append((clean_timestamp, ip, type))
                        
                        
            if data_list:
                    report = ArtifactHtmlReport('Snapchat - Return')
                    report.start_artifact_report(report_folder, 'Snapchat - IP Logs')
                    report.add_script()
                    data_headers = ('Timestamp (UTC)','IP', 'Type')
                    report.write_artifact_data_table(data_headers, data_list, file_found)
                    report.end_artifact_report()
                    
                    tsvname = f'Snapchat - IP Logs'
                    tsv(report_folder, data_headers, data_list, tsvname)
                    
                    #tlactivity = f'Kik - bind'
                    #timeline(report_folder, tlactivity, data_list, data_headers)
            else:
                    logfunc('No Snapchat - IP Logs data available')


        if filename.startswith('memories_metadata.csv'):
            data_list =[]
            with open(file_found, 'r') as f:
                    delimited = csv.reader(f, delimiter=',')
                
                    x = range(12)
                    for n in x:
                        next(delimited)
                    for item in delimited:
                        
                        id = item[0]
                        media_id = item[1]
                        encrypted = item[2]
                        source_type = item[3]
                        duration = item[4]
                        timestamp = item[5]
                        #Split timestamp date and time
                        split_timestamp = timestamp.split(' ')
                        numeric = snapchat_month(split_timestamp[1])
                        clean_timestamp = f'{split_timestamp[-1]}-{numeric}-{split_timestamp[2]} {split_timestamp[3]}'
                        data_list.append((clean_timestamp, id, media_id, encrypted, source_type, duration))
                        
                        
            if data_list:
                    report = ArtifactHtmlReport('Snapchat - Return')
                    report.start_artifact_report(report_folder, 'Snapchat - Memories')
                    report.add_script()
                    data_headers = ('Timestamp (UTC)','ID', 'Media ID', 'Encrypted', 'Source Type', 'Duration (s)')
                    report.write_artifact_data_table(data_headers, data_list, file_found)
                    report.end_artifact_report()
                
                    tsvname = f'Snapchat - Memories'
                    tsv(report_folder, data_headers, data_list, tsvname)
                
                    #tlactivity = f'Kik - bind'
                    #timeline(report_folder, tlactivity, data_list, data_headers)
            else:
                    logfunc('No Snapchat - Memories data available')

        if filename.startswith('chat.csv'):
            data_list =[]
            with open(file_found, 'r') as f:
                    delimited = csv.reader(f, delimiter=',')
        
                    x = range(1)
                    for n in x:
                        next(delimited)
                    for item in delimited:
                
                        id = item[0]
                        from_id = item[1]
                        to_id = item[2]
                        body = item[3]
                        media_id = item[5]
                        saved = item[6]
                        timestamp = item[7]
                        #Split timestamp date and time
                        split_timestamp = timestamp.split(' ')
                        numeric = snapchat_month(split_timestamp[1])
                        clean_timestamp = f'{split_timestamp[-1]}-{numeric}-{split_timestamp[2]} {split_timestamp[3]}'
                        data_list.append((clean_timestamp, id, from_id, to_id, body, media_id, saved))
                
                
            if data_list:
                    report = ArtifactHtmlReport('Snapchat - Return')
                    report.start_artifact_report(report_folder, 'Snapchat - Chats')
                    report.add_script()
                    data_headers = ('Timestamp (UTC)','ID', 'From', 'To', 'Msg. Content', 'Media ID', 'Is Saved?')
                    report.write_artifact_data_table(data_headers, data_list, file_found)
                    report.end_artifact_report()
        
                    tsvname = f'Snapchat - Chats'
                    tsv(report_folder, data_headers, data_list, tsvname)
        
                    #tlactivity = f'Kik - bind'
                    #timeline(report_folder, tlactivity, data_list, data_headers)
            else:
                    logfunc('No Snapchat - Chats data available')
            
        if filename.startswith('geo_locations.csv'):
            data_list =[]
            with open(file_found, 'r') as f:
                    delimited = csv.reader(f, delimiter=',')
            
                    x = range(4)
                    for n in x:
                        next(delimited)
                    for item in delimited:
                
                        #Split Latitude from accuracy
                        full_latitude = item[0]
                        split_latitude = full_latitude.split('±')
                        latitude = split_latitude[0].strip()
                        lat_accuracy = split_latitude[1].strip()
                        #Split longitude from accuracy
                        full_longitude = item[1]
                        split_longitude = full_longitude.split('±')
                        longitude = split_longitude[0].strip()
                        long_accuracy = split_longitude[1].strip()
                        #Split timestamp date and time
                        timestamp = item[2]
                        split_timestamp = timestamp.split(' ')
                        numeric = snapchat_month(split_timestamp[1])
                        clean_timestamp = f'{split_timestamp[-1]}-{numeric}-{split_timestamp[2]} {split_timestamp[3]}'
                        #clean_timestamp = f'{split_timestamp[-1]}-{split_timestamp[1]}-{split_timestamp[2]} {split_timestamp[3]}'
                        data_list.append((clean_timestamp, latitude, lat_accuracy, longitude, long_accuracy))           
                        
            if data_list:
                    report = ArtifactHtmlReport('Snapchat - Return')
                    report.start_artifact_report(report_folder, 'Snapchat - Geolocations')
                    report.add_script()
                    data_headers = ('Timestamp (UTC)', 'Latitude', 'Lat. Accuracy +/-', 'Longitude', 'Long. Accuracy')
                    report.write_artifact_data_table(data_headers, data_list, file_found)
                    report.end_artifact_report()
            
                    tsvname = f'Snapchat - Geolocations'
                    tsv(report_folder, data_headers, data_list, tsvname)
                    
                    #tlactivity = f'Kik - bind'
                    #timeline(report_folder, tlactivity, data_list, data_headers)
            else:
                    logfunc('No Snapchat - Geolocations data available')