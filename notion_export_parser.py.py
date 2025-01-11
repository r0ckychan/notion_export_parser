#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  notion_export_parser.py - A script to process Notion Markdown exports and remove the 32 digits from all names and links.
#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#  2. Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#  3. Neither the name of the author nor the names of its contributors may
#     be used to endorse or promote products derived from this software without
#     specific prior written permission.
#
#  Author: r0ckychan
#  Version: v0.1

import os
import re
import shutil
import sys

def copy_and_process(source_dir, target_dir):
    id_pattern = re.compile(r'(%20[0-9a-f]{32}|\s[0-9a-f]{32})')
    md_link_pattern = re.compile(r'(\[.*?\])\((.*?)(.md|.png|.jpg|.jpeg)\)')

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)

    # Copy the entire directory structure
    for root, dirs, files in os.walk(source_dir):
        rel_path = os.path.relpath(root, source_dir)
        target_root = os.path.join(target_dir, rel_path)
        os.makedirs(target_root, exist_ok=True)

        for file in files:
            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_root, file)
            shutil.copy2(source_file_path, target_file_path)

    # Process target directory recursively, renaming folders and files
    for root, dirs, files in os.walk(target_dir, topdown=False):
        # Rename files
        for file in files:
            new_name = id_pattern.sub('', file)
            if new_name != file:
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed file: {file} to {new_name}")

        # Rename directories
        for dir in dirs:
            new_name = id_pattern.sub('', dir)
            if new_name != dir:
                old_path = os.path.join(root, dir)
                new_path = os.path.join(root, new_name)
                os.rename(old_path, new_path)
                print(f"Renamed folder: {dir} to {new_name}")

    # Process markdown files and update links in target directory
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith(".md"):
                file_path = os.path.join(root, file)
                updated_lines = []
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        updated_line = md_link_pattern.sub(lambda m: f"{m.group(1)}({id_pattern.sub('', m.group(2))}{m.group(3)})", line)
                        updated_lines.append(updated_line)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(updated_lines)
                print(f"Updated links in: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: notion_export_parser.py <source_directory> <target_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2]

    if not os.path.isdir(source_directory):
        print(f"Error: Source directory '{source_directory}' does not exist.")
        sys.exit(1)

    copy_and_process(source_directory, target_directory)
    print("Renaming and markdown link updating process completed.")
