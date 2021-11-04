import unittest
import library as lb
import wallet_lib as wallet
import time

test_id = 2 # pick between test functions

class TestLibrary (unittest.TestCase):

    if test_id == 1:
        def test_send_funds(self):

            walletName = 'acdc'
            wallet01 = 'main'
            wallet02 = 'addr_test1qznxlz2nn3l8zqz00e9mx5tthf4trpc3senha8wkgg0kap80pdemwpxj47qm6tqmhxy8euajpzddxtuevprpdrum0gnsj5cuy0'
            quantity = 400
            token = 'ADA'
            # Verify initial funds from the wallets to test
            if token=='ADA':
                token = 'lovelace'
                param = 1000000
            else:
                param = 1

            balance01 = round(lb.get_balance(wallet01,token)[token])
            balance02 = round(lb.get_balance(wallet02,token)[token])

            addr_origin = lb.wallet_to_address(wallet01)
            addr_destin = lb.wallet_to_address(wallet02)
            fees = lb.tx_min_fee(addr_origin,addr_destin)
            fees = int(fees.decode('utf-8'))

            send_funds = lb.send_funds(wallet01,wallet02,quantity*param,token)

            new_balance01 = balance01 - quantity*param - fees
            new_balance02 = balance02 + quantity*param
            # 60 seconds to allow the blockchain to process and confirm the transaction
            time.sleep(60)
            actual_balance01 = lb.get_balance(wallet01,token)
            actual_balance02 = lb.get_balance(wallet02,token)

            #self.assertTrue (type(test_transactions) is dict)
            self.assertEqual(actual_balance01['lovelace'],new_balance01,"There must be some problem with the transaction")
            self.assertEqual(actual_balance02['lovelace'],new_balance02,"There must be some problem with the transaction")

    if test_id==2:
        def test_create_wallet(self):
            wallet_name = 'test6'
            passphrase = 'test123456'
            size = 24
            main ={
            'client-id': 'asjfdkjfnfdnmdlk'
        }
            mnemonic = wallet.generate_mnemonic(size)
            print(mnemonic)

            response = wallet.create_wallet(wallet_name, passphrase,mnemonic)
            print(response)
            print('id: ',response['id'],'/n', 'name: ', response['name'] )
 
            wallet_info = wallet.wallet_info(response['id'])
            print(wallet_info)
            status = wallet_info['state']['status']
            print(status)
            
            addresses = wallet.get_addresses(response['id'])
            print(addresses[0]['id'])
    if test_id==3:
        def test_delete_wallet(self):
            list_wallets=wallet.list_wallets()
            print(list_wallets)
            for k, v in list_wallets.items():
                if k==[id]:
                    wallet.delete_wallet(k)
    if test_id==4:
        def test_get_balance(self):
            wallet01 = 'addr_test1qp09lnuch5vgswuxcjlta78mlp88taudhgymyktu3qy44pk8tuvg9dmy75z2dpj0e4kzw642e3hpjt937e4t3jun3l3sftz57e'
            token = 'ADA'
            actual_balance01 = lb.get_balance(wallet01,token)
            print(actual_balance01)


    if test_id==5:
        def test_generate_nmemonic(self):
            wallet.generate_mnemonic(24)
        

            




unittest.main()