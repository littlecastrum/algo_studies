import DataNode from '../DataNode';

describe('Data structure DataNode', () => {

  it('should create a new DataNode', () => {
    const result = new DataNode();
    expect(result.data).toEqual(null)
    expect(result.next).toEqual(null)
  });

  it('should assign data to a new DataNode when set', () => {
    const result = new DataNode(1);
    expect(result.data).toEqual(1)
    expect(result.next).toEqual(null)
  });

  it('should have a reference to other DataNode when set', () => {
    const result = new DataNode(1);
    const ref = new DataNode(2);
    result.next = ref;
    expect(result.data).toEqual(1)
    expect(result.next).toEqual(ref)
  });

  it('should show the data structure when using inspect', () => {
    const result = new DataNode(1);
    expect(result.inspect()).toEqual('Data: 1\nNext: null')
  });
})