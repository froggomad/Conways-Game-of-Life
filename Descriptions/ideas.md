# Ideas

* to draw individual cells, just identify the cell as being drawn and include the circle
    ### i.e.
    * cell.drawn = true # has circle
    * cell.drawn = false # no circle
Note: This is now easily possible with the cell for position method

* let user step forward by calling increase_generation n times i.e.:

    ```
    for _ in user_num:
        self.increase_generation()
    ```
* age:
    * light green - dark green age <= 1/5
    * light orange - bright orange <= 1/2
    * bright orange - dull red <= 3/4
    * dull red - bright red >= 3/4

* for particle implementation:
    ```
        x = cell_size.width//2
        if x >= board_size.width:
            x = cell_size.width//2
        else:
            x += cell_size.width
    ```