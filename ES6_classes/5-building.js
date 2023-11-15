export default class Building {
    constructor(sqft){
        this._sqft = sqft;
    }
    get sqft() {
        return this._sqft;
      }
    
      set sqft(value) {
        if (typeof value === 'number') {
          this._amount = value;
        }
      }
    
}
