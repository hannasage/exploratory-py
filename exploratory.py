import pandas as pd
import numpy as np
import mysql.connector


# FUNCTIONS

def cleanDF(dataframe):
  col = input('Column: ')
  val = input('Value: ')

  print('Cleaning...')

  dataframe = dataframe[dataframe[col] != val]
  dataframe.index = range(len(dataframe))

  return dataframe

def filterDF(dataframe):
  col = input('Column: ')
  val = input('Value: ')

  print('Filtering...')

  dataframe = dataframe[dataframe[col] == val]
  dataframe.index = range(len(dataframe))

  return dataframe

def exportDF(dataframe):
  file_name_input = input('File Name: ')
  file_name = file_name_input + ".csv"
  path_input = input('Path: C:\\Users\\Kevin\\Documents')
  path = 'C:\\Users\\Kevin\\Documents' + path_input + '\\' + file_name

  print('Exporting...')

  dataframe.to_csv(path)

def column_selection():
  selected = []
  col_in = input('Select column: ')
  while col_in != '' and col_in != 'C' and col_in != 'c':
    selected.append(col_in)
    col_in = input('Select another column, or type \'C\' to continue: ')

  return selected

def command_listener():
  global df_cols
  cmd_str = 'Enter a command (filter, clean, export, or quit): '
  command = input(cmd_str)
  while command != 'quit':
    if command.lower() == 'filter':
      # Filtering
      df_cols = filterDF(df_cols)
      print(df_cols)
      command = input(cmd_str)
    elif command.lower() == 'clean':
      # Cleaning
      df_cols = cleanDF(df_cols)
      print(df_cols)
      command = input(cmd_str)
    elif command.lower() == 'export':
      # Export as CSV
      exportDF(df_cols)
      command = input(cmd_str)
    elif command.lower() == 'quit':
      exit()
    else:
      command = input('Invalid request.\n' + cmd_str)


# SCRIPT STARTS HERE

mydb = mysql.connector.connect(
  host="elder.cpmihxwddknw.us-east-2.rds.amazonaws.com",
  user="root",
  passwd="6MurP2rrVZuKv9egwF8Q",
  database="innodb"
)

table = input('Enter table: ')

df = pd.read_sql(('SELECT * FROM %s' % table), mydb)
print(df.columns)

cols = column_selection()
df_cols = df[cols]

print('\n=================  %s  =================\n' % table)
print(df_cols)

command_listener()


