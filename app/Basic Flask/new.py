create table product96(
ID varchar2(10),
cust XMLTYPE
);


insert into Product96 values(
1,xmltype('
<customer>
<Tcustomer>
<Rcustomer>
<cid>c1</cid>
<cname>Rohan</cname>
<city>Mumbai</city>
</Rcustomer>
<Rcustomer>
<cid>c1</cid>
<cname>Kamlesh</cname>
<city>Thane</city>
</Rcustomer>
</Tcustomer>
<Torder>
<Rorder>
<oid>o1</oid>
<cid>c1</cid>
<odate>10-Aug-2018</odate>
</Rorder>
<Rorder>
<oid>o2</oid>
<cid>c2</cid>
<odate>28-Feb-2018</odate>
</Rorder>
</Torder>
<Titem>
<Ritem>
<oid>01</oid>
<product>p001</product>
<qty>14</qty>
</Ritem>
<Ritem>
<oid>02</oid>
<product>p002</product>
<qty>16</qty>
</Ritem>
</Titem>
</customer>
')
);

insert into Product96 values(
2,xmltype('
<customer>
<Tcustomer>
<Rcustomer>
<cid>c1</cid>
<cname>shree</cname>
<city>Mumbai</city>
</Rcustomer>
<Rcustomer>
<cid>c2</cid>
<cname>rajesh</cname>
<city>Mumbai</city>
</Rcustomer>
</Tcustomer>
<Torder>
<Rorder>
<oid>o2</oid>
<cid>c2</cid>
<odate>15-Aug-2018</odate>
</Rorder>
<Rorder>
<oid>o3</oid>
<cid>c3</cid>
<odate>14-Feb-2018</odate>
</Rorder>
</Torder>
<Titem>
<Ritem>
<oid>02</oid>
<product>p002</product>
<qty>14</qty>
</Ritem>
<Ritem>
<oid>02</oid>
<product>p003</product>
<qty>16</qty>
</Ritem>
</Titem>
</customer>
')
);


insert into Product96 values(
3,xmltype('
<customer>
<Tcustomer>
<Rcustomer>
<cid>c2</cid>
<cname>Jay</cname>
<city>Mumbai</city>
</Rcustomer>
<Rcustomer>
<cid>c3</cid>
<cname>Prakash</cname>
<city>Mumbai</city>
</Rcustomer>
</Tcustomer>
<Torder>
<Rorder>
<oid>o3</oid>
<cid>c3</cid>
<odate>1-Aug-2018</odate>
</Rorder>
<Rorder>
<oid>o4</oid>
<cid>c4</cid>
<odate>5-Feb-2018</odate>
</Rorder>
</Torder>
<Titem>
<Ritem>
<oid>03</oid>
<product>p003</product>
<qty>14</qty>
</Ritem>
<Ritem>
<oid>03</oid>
<product>p004</product>
<qty>16</qty>
</Ritem>
</Titem>
</customer>
')
);

select p.cust.extract('/Tcustomer/Torder/text()[oid="o3"]').getStringVal() "Orders" from Product96;

Select p.CUST.extract('/Tcustomer').getStringVal() from Product96 p where
p.CUST.extract('//Tcustomer/cid/text()').getStringVal() = 'c1';