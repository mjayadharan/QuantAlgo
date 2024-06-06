class order_logistics:
    
    def __init__(self,assets,in_positions,entry_prices,orders,order_id,current_price,index,w8):
        self.assets = assets
        self.in_positions = in_positions
        self.entry_prices = entry_prices
        self.orders = orders
        self.order_id = order_id
        self.current_price = current_price
        self.index = index
        self.w8 = w8


    def order_place(self):
        for i in range(len(self.assets)):
            asset_name = self.assets[i]
            if asset_name not in self.orders:
                self.orders[asset_name] = []  # Initialize orders for this asset if not present
            if asset_name not in self.in_positions:            
                self.in_positions[asset_name] = []
            if asset_name not in self.entry_prices:            
                self.entry_prices[asset_name] = []
            self.entry_prices[asset_name].append(self.current_price[asset_name])
            if self.w8[asset_name][-1] > 0:
                self.orders[asset_name].append((self.order_id[asset_name][-1],self.index[asset_name], 'BUY PLACED', self.entry_prices[asset_name]))
            else:
                self.orders[asset_name].append((self.order_id[asset_name][-1],self.index[asset_name], 'SELL PLACED', self.entry_prices[asset_name]))
            self.in_positions[asset_name].append(True)
            self.order_id[asset_name].append(self.order_id[asset_name][-1]+1)
                

    def order_profit(self):
        
        current_profit = 0
        for i in range(len(self.assets)):
            asset_name = self.assets[i]
            for j in range(len(self.entry_prices[asset_name])):
                if (self.in_positions[asset_name][j]==True):
                    current_profit += self.w8[asset_name][j]*(self.current_price[asset_name] - self.entry_prices[asset_name][j])             

        return current_profit


    def order_clear(self):

        for i in range(len(self.assets)):
            asset_name = self.assets[i]
            k = len(self.in_positions[asset_name])
            for j in range(k):
                if self.w8[asset_name][j] > 0:
                    self.orders[asset_name].append((self.order_id[asset_name][j-k-1],self.index[asset_name], 'BUY CLOSED', self.current_price[asset_name]))
                else:
                    self.orders[asset_name].append((self.order_id[asset_name][j-k-1],self.index[asset_name], 'SELL CLOSED', self.current_price[asset_name]))
        self.in_positions = {}
        self.entry_prices = {}
        self.w8 = {}
    