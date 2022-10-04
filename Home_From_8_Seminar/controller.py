import view
import imp
import exp
import logger

def run():
     temp = view.choice()
     if temp == 1:
          print ('Новый сотрудник')
          entry = imp.record() # Запись в справочник
          logger.log_to_file(entry)
          run()
     if temp == 2:
          print ('\n Поиск сотрудника\n' )
          entry = exp.search() # Поиск в справочнике
          logger.reading_file(entry)
          run()
     if temp == 3:
          print ('n=== ВСЕ СОТРУДНИКИ ===\n')
          logger.read_all_file()  
          run()
     if temp == 4:
          print('\n Работа завершена \n')
          