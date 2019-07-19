export type DataType =  any | null;
export type NodeRefType = DataNode | null

export default class DataNode {
  private _data: DataType
  private _next: NodeRefType

  constructor(value: DataType = null, node: NodeRefType = null) {
    this.data = value;
    this.next = node
  }

  get data(): any {
    return this._data;
  }

  set data(value: any) {
    this._data = value;
  }

  get next(): DataNode {
    return this._next;
  }

  set next(node: DataNode) {
    this._next = node;
  }

  public inspect() {
    return `Data: ${this.data}\nNext: ${this.next ? this.next.data : null}`
  }
}