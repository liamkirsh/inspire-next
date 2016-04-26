/*
 * This file is part of Invenio.
 * Copyright (C) 2016 CERN.
 *
 * Invenio is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of the
 * License, or (at your option) any later version.
 *
 * Invenio is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Invenio; if not, write to the Free Software Foundation, Inc.,
 * 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
 */

define(
  [
    'jquery',
    'flight'
  ],
  function(
    $,
    flight) {

    "use strict";

    return flight.component(DetailsPage);

    function DetailsPage() {
      // The logic here is:
      // 1. If there is a next page, go there
      // 2. If there is not a next page, go to the previous one.
      // 3. If that was the last record (no next/previous pages) go to the main list.
      this.changePage = function() {
        var next_object_id = this.$node.data('next-objectid');
        if (next_object_id) {
          window.location.href = this.$node.data('ui-url') + "/details/" + next_object_id;
        } else {
          window.location.href = this.$node.data('ui-url') + "/list";
        }
      };

      this.after('initialize', function() {
        this.on(document, "changePage", this.changePage);
        console.log("Details Page init");
      });
    }
});
